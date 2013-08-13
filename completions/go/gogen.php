#!/usr/bin/env php
<?php


$src = file_get_contents("go1.txt");
genSource("go1_", $src);

$src = file_get_contents("go1.1.txt");
genSource("go1.1_", $src);

function createFile($fpref, $name, $contents) {
	$out = '{' . "\n    " . '"extendedConfidence": false,' . "\n    " . '"items": [';
	$pref = "\n";
	foreach ($contents as $func) {
		list($fn, $o) = explode("(", $func, 2);
		$out .= $pref . '        "' . trim($fn) . '"'; 
		$pref = ",\n";
	}
	$out .= "\n    " . '],' . "\n    " . '"icon": "function",' . "\n    " . '"prototypes": [';
	$pref = "\n";
	foreach ($contents as $func) {
		list($fn, $o) = explode("(", $func, 2);
		$fn = trim($fn);
		
		list($fp, $ft) = explode(") ", $o, 2);
		$fp = explode(", ", $fp);
		$fp = implode(" , ", $fp);
		
		$ft = "any";
		
		$out .= $pref . "        " . '" ' . $ft . ' ' . $fn . ' ( ' . $fp . ' )"'; 
		$pref = ",\n";
	}
	$out .= "\n    " . '],' . "\n    " . '"prefix": "' . $name . '."' . "\n" . '}';
	file_put_contents($fpref . $name . ".json", $out);
}


function genSource($pref, $src) {
	$lines = explode("\n", $src);
	
	$package = "";
	$buffer = array();
	
	foreach ($lines as $line) {
		list($p, $o) = explode(",", $line, 2);
		
		//Clean Name
		$p = explode(" ", $p)[1];
		$p = explode("/", $p);
		$p = $p[count(p) - 1];
		
		if ($p != $package) {
			if ($package != "") {
				createFile($pref, $package, $buffer);
			}
			$buffer = array();
			$package = $p;
		}
		
		//Clean other
		$o = trim($o);
		list($t, $o) = explode(" ", $o, 2);
		
		if ($t == "func") {
			array_push($buffer, $o);
		}
	}
}



