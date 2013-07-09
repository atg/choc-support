module.exports = {
  reporter: function (errors) {
    var output = [];
    
    for (var i = 0, len = errors.length; i < len; i++) {
      var error = errors[i].error;
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
      
      output.push({
        path: '',
        line: error.line,
        message: error.reason + ' (' + error.code + ')',
        column: '' + error.character,
        type: type
      });
    }
    
    console.log(JSON.stringify(output));
  }
};