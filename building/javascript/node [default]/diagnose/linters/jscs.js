var defaults = require('lodash.defaults');
var configFile = require('jscs/lib/cli-config');
var Checker = require('jscs/lib/checker');

module.exports = function(ctx) {
  var cfg = configFile.load(ctx.rcpath);

  var checker = new Checker();

  checker.getConfiguration().registerDefaultRules();

  checker.configure(cfg);

  var occs = checker.checkString(ctx.source, ctx.filename).getErrorList();

  return occs.map(function(occ) {
    return {
      line: Number(occ.line),
      message: occ.message,
      column: Number(occ.column),
      type: 'warning',
      source: 'jscs'
    };
  }).filter(function(occ) {
    return !(/^Unsupported\srule\:/).test(occ.message || '');
  });
};

module.exports.config = function(ctx) {
  return defaults({
    filenames: ['.%src', '.%s.json', '.%s.yaml'],
    pkgAttr: 'jscsConfig'
  }, ctx);
};