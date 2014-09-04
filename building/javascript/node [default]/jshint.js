var jshint = require('jshint/src/cli');

var reporter = function(fn) {
  return function(diagnostics) {
    fn(null, diagnostics.map(function(diagnostic) {
      var error = diagnostic.error;
      var type = 'warning';

      switch(error.code.charAt(0)) {
        case 'W':
          type = 'warning'; break;
        case 'E':
          type = 'error'; break;
      }

      if (error.reason.indexOf('Expected') !== -1 || error.reason.indexOf('Unmatched') !== -1) {
        type = 'error';
      }

      if (error.code === 'W015' || error.code === 'W084') {
        type = 'warning';
      }

      return {
        path: '',
        line: error.line,
        message: error.reason + ' (' + error.code + ')',
        column: '' + error.character,
        type: type,
        source: 'jshint'
      };
    }));
  };
};

var diagnose = function(filepath, configpath, fn){
  jshint.run({
    args: [filepath],
    config: jshint.loadConfig(configpath),
    ignores: [],
    extensions: '',
    verbose: null,
    extract: 'never',
    filename: null,
    reporter: reporter(fn)
  });
}

module.exports = function(filepath, configpath, fn) {
  try {
    diagnose(filepath, configpath, fn);
  } catch (err) {
    fn(err);
  }
};