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
      
      if (error.reason.indexOf('Expected') !== -1 || error.reason.indexOf('Expected') !== -1) {
          type = 'error'
      }
      if (error.reason.indexOf('Expected a conditional expression and instead saw an assignment') !== -1) {
          type = 'warning'
      }
      
      output.push({
        path: '',
        line: error.line,
        message: error.reason,
        column: '' + error.character,
        type: type
      });
    }
    
    console.log(JSON.stringify(output));
  }
};