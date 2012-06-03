#!/bin/bash

VERB="REPL"

# Helpers shared by all of Python's build scripts go in here.
source common.sh

cd "$CHOC_RUN_DIRECTORY"

if [[ "x$CHOC_REPL" -ne "x" ]]; then
    echo -e ">>> Running custom script.\n"
    echo "$CHOC_REPL" > $CHOC_TEMPFILE_1
    exec $CHOC_TEMPFILE_1
fi

echo -e ">>> Running:\n>>>\tpython -i $CHOC_FILE\n"
python -i $CHOC_FILE
