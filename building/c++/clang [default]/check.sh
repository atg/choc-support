clang++ -x c -std=c99 -fsyntax-only -fno-color-diagnostics "$CHOC_FILE" 2>&1 # we can't take from stdin here since clang has no way to check syntax without trying to follow #includes
