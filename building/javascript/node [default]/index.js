var diagnose = require('./diagnose');
var fs = require('fs');

diagnose({
  home: process.env['HOME'],
  cwd: process.env['CHOC_PROJECT_DIR'],
  source: fs.readFileSync(process.env['CHOC_FILE'], 'utf-8'),
  filename: process.env['CHOC_PROJECT_FILE']
}, function(err, report) {
  if (err) {
    throw err;
  }

  console.log(JSON.stringify(report, null, 2));
});
