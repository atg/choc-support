var get = require('lodash.get');
var requireDir = require('require-dir');
var forceArray = require('force-array');
var clone = require('lodash.clonedeep');
var find = require('lodash.find');
var format = require('format');
var path = require('path');
var async = require('async');
var fs = require('fs');

var lintersPath = path.join(__dirname, 'linters');
var linters = requireDir(lintersPath);

var linterNames = fs.readdirSync(lintersPath).map(function(v) {
  return path.basename(v, path.extname(v));
});

var detectConfig = function(ctx, fn) {
  if (ctx.pkgAttr && ctx.pkg[ctx.pkgAttr]) {
    return fn(null, [
      ctx.pkgPath
    ]);
  }

  var filenames = ctx.filenames.map(function(filename) {
    return format(filename, ctx.linter);
  });

  async.filter(filenames.map(function(filename) {
    return path.join(ctx.cwd, filename);
  }), function(filename, fn) {
    fs.exists(filename, function(exists) {
      fn(null, exists ? filename : false);
    });
  }, fn);
};

var existent = function(ctx) {
  return function(fn) {
    return detectConfig(linters[ctx.linter].config(ctx), fn);
  };
};

var checker = function(dirname) {
  var pkgPath = path.join(dirname, 'package.json');
  var pkg = {};

  try {
    pkg = require(pkgPath);
  } catch (err) {
    // console.error('%s not found', pkgPath);
  }

  return linterNames.reduce(function(sum, name) {
    sum[name] = existent({
      cwd: dirname,
      linter: name,
      pkgPath: pkgPath,
      pkg: pkg
    });

    return sum;
  }, {});
};

var files = function(ctx, fn) {
  async.parallel({
    local: function(fn) {
      async.parallel(checker(ctx.cwd), fn);
    },
    global: function(fn) {
      async.parallel(checker(ctx.home), fn);
    },
    fallback: function(fn) {
      async.parallel(checker(__dirname), fn);
    }
  }, fn);
};

var stages = function() {
  var stages = [
    'eslint', [
      'jshint',
      'jscs'
    ]
  ];

  var stage = function(ctx) {
    return function(v) {
      return forceArray(v).map(function(v) {
        return format('%s.%s', ctx, v);
      });
    };
  };

  var local = clone(stages).map(stage('local'));
  var fallback = clone(stages).map(stage('fallback'));
  var global = clone(stages).map(stage('global'));

  return local.concat(global).concat(fallback);
};

module.exports = function(ctx, fn) {
  files(ctx, function(err, files) {
    if (err) {
      return fn(err);
    }

    var stage = find(stages(), function(stage) {
      return stage.some(function(v) {
        return get(files, v).length;
      });
    });

    fn(null, stage.map(function(v) {
      return {
        rcpath: get(files, v)[0],
        linter: v.split(/\./).pop()
      }
    }).filter(function(cfg) {
      return cfg.rcpath;
    }));
  });
};
