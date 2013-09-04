#!/usr/bin/env php
<?php

$packages = array("archive/tar", "archive/zip", "bufio", "builtin", "bytes", "compress/bzip2", "compress/flate", "compress/gzip", "compress/lzw", "compress/zlib", "container/heap", "container/list", "container/ring", "crypto/aes", "crypto/cipher", "crypto/des", "crypto/dsa", "crypto/ecdsa", "crypto/elliptic", "crypto/hmac", "crypto/md5", "crypto/rand", "crypto/rc4", "crypto/rsa", "crypto/sha1", "crypto/sha256", "crypto/sha512", "crypto/subtle", "crypto/tls", "crypto/x509", "crypto/x509/pkix", "database/sql", "database/sql/driver", "debug/dwarf", "debug/elf", "debug/gosym", "debug/macho", "debug/pe", "encoding/ascii85", "encoding/asn1", "encoding/base32", "encoding/base64", "encoding/binary", "encoding/csv", "encoding/gob", "encoding/hex", "encoding/json", "encoding/pem", "encoding/xml", "errors", "expvar", "flag", "fmt", "go/ast", "go/build", "go/doc", "go/format", "go/parser", "go/printer", "go/scanner", "go/token", "hash/adler32", "hash/crc32", "hash/crc64", "hash/fnv", "hash", "html", "html/template", "image", "image/color", "image/draw", "image/gif", "image/jpeg", "image/png", "index/suffixarray", "io", "io/ioutil", "log", "log/syslog", "math", "math/big", "math/cmplx", "math/rand", "mime", "mime/multipart", "net", "net/http", "net/http/cgi", "net/http/cookiejar", "net/http/fcgi", "net/http/httptest", "net/http/httputil", "net/http/pprof", "net/mail", "net/rpc", "net/rpc/jsonrpc", "net/smtp", "net/textproto", "net/url", "os", "os/exec", "os/signal", "os/user", "path", "path/filepath", "reflect", "regexp", "regexp/syntax", "runtime", "runtime/cgo", "runtime/debug", "runtime/pprof", "runtime/race", "sort", "strconv", "strings", "sync", "sync/atomic", "syscall", "testing", "testing/iotest", "testing/quick", "text/scanner", "text/tabwriter", "text/template", "text/parse", "time", "unicode", "unicode/utf16", "unicode/utf8", "unsafe");

$command = "godoc -templates=./ ";

foreach ($packages as $package) {
	$lines = array();
	exec($command . $package, $lines);
	$src = implode(" ", $lines);
	$src = str_replace(",REMOVE_COMMA_END_OF_LINE", "", $src);
	
	$docs = json_decode($src);
	
	//Get Name
	$name = explode("/", $package);
	$name = $name[count($name) - 1];
	
	$fname = "go_" . implode("_", explode("/", $package));
	
	if (isset($docs->funcs)) {
		$functions = array();
		$pr = array();
		foreach ($docs->funcs as $k => $v) {
			array_push($functions, $k);
			$v = explode(") ", $v . " ", 2);
			$v = $v[0];
			
			list($fn, $o) = explode("(", $v, 2);
			$fp = implode(" , ", explode(", ", $o));
			array_push($pr, " any " . $k . " ( " . $fp . " )");
		}
		$fs = array(
			"icon" => "function",
			"extendedConfidence" => true,
			"items" => $functions,
			"prototypes" => $pr
		);
		if ($name != "builtin") {
			$fs["prefix"] = $name . ".";
		}
		file_put_contents($fname . "_funcs.json", json_encode($fs));
	}
	
	if (isset($docs->types)) {
		$types = array(
			"icon" => "class",
			"extendedConfidence" => true,
			"items" => $docs->types
		);
		if ($name != "builtin") {
			$types["prefix"] = $name . ".";
		}
		file_put_contents($fname . "_types.json", json_encode($types));
	}
	
	if (isset($docs->vars)) {
		$vars = array(
			"icon" => "variable",
			"type" => "variable",
			"extendedConfidence" => true,
			"items" => $docs->vars
		);
		if ($name != "builtin") {
			$vars["prefix"] = $name . ".";
		}
		file_put_contents($fname . "_vars.json", json_encode($vars));
	}
	
	if (isset($docs->const)) {
		$constants = array(
			"icon" => "constant",
			"type" => "constant",
			"extendedConfidence" => true,
			"items" => $docs->const,
		);
		if ($name != "builtin") {
			$constants["prefix"] = $name . ".";
		}
		file_put_contents($fname . "_constants.json", json_encode($constants));
	}
}


