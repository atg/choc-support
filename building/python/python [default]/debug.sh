#!/bin/bash

VERB="Debugging"

# Helpers shared by all of Python's build scripts go in here.
source common.sh

cd "$CHOC_RUN_DIRECTORY"

if [[ "x$CHOC_DEBUG" -ne "x" ]]; then
    echo -e ">>> Running custom script.\n"
    echo "$CHOC_DEBUG" > $CHOC_TEMPFILE_1
    exec $CHOC_TEMPFILE_1
fi

echo -e ">>> Running:\n>>>\tpython -m pdb $CHOC_FILE\n"
python -m pdb $CHOC_FILE
