if (MATCH_LANG(@"c") || MATCH_LANG(@"c++") || MATCH_LANG(@"objc") || MATCH_LANG(@"objc++") || MATCH_LANG(@"actionscript") || MATCH_LANG(@"csharp") || MATCH_LANG(@"go") || MATCH_LANG(@"java") || MATCH_LANG(@"js") || MATCH_LANG(@"lemon") || MATCH_LANG(@"objj") || MATCH_LANG(@"pike") || MATCH_LANG(@"scala") || MATCH_LANG(@"scss") || MATCH_LANG(@"verilog")) {
    MATCH_LINE_COMMENT(@"//");
    MATCH_BLOCK_COMMENT(@"/*", @"*/");
}
else if (MATCH_LANG(@"ada")) {
    MATCH_LINE_COMMENT(@"--");
}
else if (MATCH_LANG(@"applescript")) {
    MATCH_LINE_COMMENT(@"--");
    MATCH_BLOCK_COMMENT(@"(*", @"*)");
}
else if (MATCH_LANG(@"asm") || MATCH_LANG(@"clojure") || MATCH_LANG(@"lisp")) {
    MATCH_LINE_COMMENT(@";");
}
else if (MATCH_LANG(@"coffeescript")) {
    MATCH_LINE_COMMENT(@"#");
    MATCH_BLOCK_COMMENT(@"///", @"///");
}
else if (MATCH_LANG(@"css")) {
    MATCH_BLOCK_COMMENT(@"/*", @"*/");
}
else if (MATCH_LANG(@"d")) {
    MATCH_LINE_COMMENT(@"//");
    MATCH_BLOCK_COMMENT(@"/*", @"*/");
    MATCH_BLOCK_COMMENT(@"/+", @"+/");
}
else if (MATCH_LANG(@"erlang") || MATCH_LANG(@"latex") || MATCH_LANG(@"tex") || MATCH_LANG(@"postscript")) {
    MATCH_LINE_COMMENT(@"%");
}
else if (MATCH_LANG(@"fortran")) {
    MATCH_LINE_COMMENT(@"!");
}
else if (MATCH_LANG(@"fsharp")) {
    MATCH_LINE_COMMENT(@"//");
    MATCH_BLOCK_COMMENT(@"(*", @"*)");
}
else if (MATCH_LANG(@"haml")) {
    MATCH_LINE_COMMENT(@"-#");
}
else if (MATCH_LANG(@"haskell")) {
    MATCH_LINE_COMMENT(@"--");
    MATCH_BLOCK_COMMENT(@"{-", @"-}");
}
else if (MATCH_LANG(@"io")) {
    MATCH_LINE_COMMENT(@"#");
    MATCH_BLOCK_COMMENT(@"/*", @"*/");
}
else if (MATCH_LANG(@"lua")) {
    MATCH_LINE_COMMENT(@"--");
    MATCH_BLOCK_COMMENT(@"--[[", @"--]]");
}
else if (MATCH_LANG(@"ocaml")) {
    MATCH_BLOCK_COMMENT(@"(*", @"*)");
}
else if (MATCH_LANG(@"oz") || MATCH_LANG(@"prolog")) {
    MATCH_LINE_COMMENT(@"%");
    MATCH_BLOCK_COMMENT(@"/*", @"*/");
}
else if (MATCH_LANG(@"pascal")) {
    MATCH_LINE_COMMENT(@"//");
    MATCH_BLOCK_COMMENT(@"{", @"}");
}
else if (MATCH_LANG(@"perl") || MATCH_LANG(@"r") || MATCH_LANG(@"ragel") || MATCH_LANG(@"shell") || MATCH_LANG(@"tcl")) {
    MATCH_LINE_COMMENT(@"#");
}
else if (MATCH_LANG(@"php")) {
    MATCH_LINE_COMMENT(@"//");
    MATCH_LINE_COMMENT(@"#");
    MATCH_BLOCK_COMMENT(@"/*", @"*/");
}
else if (MATCH_LANG(@"python")) {
    MATCH_LINE_COMMENT(@"#");
    MATCH_BLOCK_COMMENT(@"\"\"\"", @"\"\"\"");
}
else if (MATCH_LANG(@"rexx")) {
    MATCH_BLOCK_COMMENT(@"/*", @"*/");
}
else if (MATCH_LANG(@"ruby")) {
    MATCH_LINE_COMMENT(@"#");
    MATCH_BLOCK_COMMENT(@"=begin", @"=end");
}
else if (MATCH_LANG(@"sass")) {
    MATCH_LINE_COMMENT(@"//");
}
else if (MATCH_LANG(@"scheme")) {
    MATCH_LINE_COMMENT(@";");
    MATCH_BLOCK_COMMENT(@"#|", @"|#");
}
else if (MATCH_LANG(@"selfml")) {
    MATCH_LINE_COMMENT(@"#");
    MATCH_BLOCK_COMMENT(@"{#", @"#}");
}
else if (MATCH_LANG(@"smalltalk")) {
    MATCH_BLOCK_COMMENT(@"\"", @"\"");
}
else if (MATCH_LANG(@"vhdl")) {
    MATCH_LINE_COMMENT(@"--");
}
else if (MATCH_LANG(@"furrow")) {
    MATCH_LINE_COMMENT(@"--");
}
else if (MATCH_LANG(@"yaml")) {
    MATCH_LINE_COMMENT(@"#");
}
else if (MATCH_LANG(@"sql")) {
    MATCH_LINE_COMMENT(@"--");
    MATCH_BLOCK_COMMENT(@"/*", @"*/");
}
else if (MATCH_LANG(@"html") || MATCH_LANG(@"textile") || MATCH_LANG(@"xml") || MATCH_LANG(@"xslt")) {
    MATCH_BLOCK_COMMENT(@"<!--", @"-->");
}
