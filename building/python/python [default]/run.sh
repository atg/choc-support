#!/bin/bash

VERB="Running"

# Helpers shared by all of Python's build scripts go in here.
source common.sh

cd "$CHOC_RUN_DIRECTORY"

if [[ "x$CHOC_RUN" -ne "x" ]]; then
    echo -e ">>> Running custom script.\n"
    echo "$CHOC_RUN" > $CHOC_TEMPFILE_1
    exec $CHOC_TEMPFILE_1
fi

echo -e ">>> Running:\n>>>\tpython $CHOC_FILE\n"
python $CHOC_FILE
