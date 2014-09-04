var argv = require('minimist')(process.argv.slice(2));
var jshint = require('./jshint');
var jscs = require('./jscs');

var filepath = argv._.shift();
var diagnostics = [];

var reporter = function() {
  console.log(JSON.stringify(diagnostics.filter(function(diagnostic) {
    return diagnostic.line !== 0;
  }).sort(function(a, b) {
    if ((a.line === b.line) && (a.source == b.source)) {
      return Number(a.column) - Number(b.column)
    }

    if (a.line === b.line) {
      return a.source === 'jshint' ? -1 : 1
    }

    return a.line - b.line;
  }), null, 2));
};

var onJSCS = function(err, res) {
  if (err) console.error(err.stack);
  diagnostics = diagnostics.concat(Array.isArray(res) ? res : []);
  reporter();
};

var onJSHint = function(err, res) {
  if (err) console.error(err.stack);

  diagnostics = diagnostics.concat(Array.isArray(res) ? res : []);
  jscs(filepath, argv['jscs-config'], onJSCS);
};

jshint(filepath, argv['jshint-config'], onJSHint);


var a = {
  b : 'a',
  c: f
};



