g++ -x c -std=c++11 -fsyntax-only "$CHOC_FILE" 2>&1 # We can't take from stdin here, since gcc has no way to check syntax without trying to check includes
