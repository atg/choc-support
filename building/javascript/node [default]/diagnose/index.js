var config = require('./config');
var defaults = require('lodash.defaults');
var flatten = require('lodash.flatten');
var requireDir = require('require-dir');
var path = require('path');

var linters = requireDir(path.join(__dirname, 'linters'));

var lint = function(ctx) {
  return function(cfg) {
    try {
      return linters[cfg.linter](defaults(cfg, ctx));
    } catch (err) {
      console.error(err);
      return [];
    }
  };
};

module.exports = function(ctx, fn) {
  config(ctx, function(err, cfgs) {
    if (err) {
      return fn(err);
    }

    fn(null, flatten(cfgs.map(lint(ctx))).filter(Boolean).sort(function(a, b) {
      return a.line - b.line;
    }));
  });
};

