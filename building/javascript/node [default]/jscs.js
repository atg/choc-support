var Checker = require('jscs/lib/checker');
var configFile = require('jscs/lib/cli-config');
var preset = require('jscs/lib/options/preset');
var fs = require('fs');
var path = require('path');
var vow = require('vow');
var flatten = require('underscore').flatten;

var reporter = function(errorsCollection) {
  return flatten(errorsCollection.map(function(errors) {
    return errors.getErrorList().map(function(error) {
      return {
        path: '',
        line: error.line,
        message: error.message,
        column: '' + error.column,
        type: 'warning',
        source: 'jscs'
      }
    });
  }));
};

var diagnose = function(filepath, configpath, fn){
  var checker = new Checker();
  var config = configFile.load(configpath);
  checker.registerDefaultRules();
  checker.configure(config);

  vow.all([filepath].map(checker.checkPath, checker)).then(function(results) {
    var diagnostics = [];

    try {
      var diagnostics = reporter([].concat.apply([], results));
    } catch (err) {
      return fn(err);
    }

    fn(null, diagnostics);
  }).fail(fn);
}

module.exports = function(filepath, configpath, fn) {
  try {
    diagnose(filepath, configpath, fn);
  } catch (err) {
    fn(err);
  }
};