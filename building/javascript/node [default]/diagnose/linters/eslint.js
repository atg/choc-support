var defaults = require('lodash.defaults');
var Config = require('eslint/lib/config');
var Linter = require('eslint/lib/eslint');
var ModuleResolver = require('eslint/lib/util/module-resolver');
var Plugins = require('eslint/lib/config/plugins');
var Module = require('module');
var path = require('path');

var PLUGIN_NAME_PREFIX = 'eslint-plugin-';

var mokeyPatchResolve = function(cwd, fn) {
  var cwdnm = path.join(cwd, 'node_modules');

  var backups = {
    ModuleResolver: ModuleResolver.prototype.resolve,
    Plugins: Plugins.load
  };

  var patch = function(lookupPaths, pathname) {
    var lp = lookupPaths.concat();
    lp.unshift(pathname);
    return lp;
  };

  Plugins.load = function(pluginName) {
    var pluginNamespace = Plugins.getNamespace(pluginName);
    var pluginNameWithoutNamespace = Plugins.removeNamespace(pluginName);
    var pluginNameWithoutPrefix = Plugins.removePrefix(pluginNameWithoutNamespace);
    var plugins = Plugins.getAll();

    var plugin = null;

    if (!plugins[pluginNameWithoutPrefix]) {
      try {
        var lp = patch(module.paths, cwdnm);
        var name = pluginNamespace + PLUGIN_NAME_PREFIX + pluginNameWithoutPrefix;
        var pluginPath = Module._findPath(name, lp);
        plugin = require(pluginPath);
      } catch (err) {
        err.message = 'Failed to load plugin ' + pluginName + ': ' + err.message;
        err.messageTemplate = 'plugin-missing';
        err.messageData = {
          pluginName: pluginNameWithoutPrefix
        };

        throw err;
      }

      Plugins.define(pluginName, plugin);
    }
  };

  ModuleResolver.prototype.resolve = function(name, extraLookupPath) {
    var lp = patch(patch(this.options.lookupPaths, cwdnm), extraLookupPath);
    var result = Module._findPath(name, lp);

    if (!result) {
      throw new Error('Cannot find module \'' + name + '\'');
    }

    return result;
  };

  return fn(function() {
    // restore
    ModuleResolver.prototype.resolve = backups.ModuleResolver;
    Plugins.load = backups.Plugins;
  });
};

module.exports = function(ctx) {
  var cfg = mokeyPatchResolve(ctx.cwd, function() {
    return new Config({
      configFile: ctx.rcpath,
      extensions: ['.js', '.jsx'],
      ignorePath: path.join(ctx.cwd, '.eslintignore'),
      cwd: ctx.cwd
    })
  });

  var occs = Linter.verify(ctx.source, cfg.useSpecificConfig, {
    filename: ctx.filename,
    allowInlineConfig: true
  });

  return occs.map(function(occ) {
    return {
      line: Number(occ.line),
      message: occ.message,
      column: Number(occ.column),
      type: 'warning',
      source: 'eslint'
    };
  });
};

module.exports.config = function(ctx) {
  return defaults({
    filenames: ['.%src.js', '.%src.yaml', '.%src.yml', '.%src.json', '.%src'],
    pkgAttr: 'eslintConfig'
  }, ctx);
};