var defaults = require('lodash.defaults');
var forceArray = require('force-array');
var cli = require('jshint/src/cli');
var jshint = require('jshint').JSHINT;

var type = {
  W: 'warning',
  E: 'error'
};

module.exports = function(ctx) {
  var cfg = cli.loadConfig(ctx.rcpath);

  jshint(ctx.source, cfg);

  return forceArray(jshint.errors).map(function(occ) {
    return {
      line: Number(occ.line),
      message: occ.reason,
      column: Number(occ.character),
      type: type[occ.code.charAt(0)],
      source: 'jshint'
    };
  }).filter(function(occ) {
    return occ.line > 0;
  });
};

module.exports.config = function(ctx) {
  return defaults({
    filenames: ['.%src', '.%s.json']
  }, ctx);
};
