#!/usr/bin/env node
var jshint, input;

/* First we open the `jshint` module */
try {
	jshint = require ('jshint').JSHINT;
} catch (e) {
	process.stderr.write ("Error: Could not find `jshint` Node.js module.\n");
	process.exit (1);
}

/* Next we read the input */
input = "";
process.stdin.resume();
process.stdin.setEncoding('utf8');
process.stdin.on('data', function (chunk) {
	input += String(chunk);
});
process.stdin.on('end', function () {
	var result, error;

	/* Here we have read the input, now we jshint it */
	result = jshint (input /* options, globals */);
	if (!result) {
		for (var i = 0, len = jshint.errors.length; i < len; i++) {
			error = jshint.errors[i];
			process.stdout.write (
				"Line " + error.line + ", " +
				"column " + error.character + ": " +
				error.reason + "\n");
		}
	}

	process.exit (0);
});
