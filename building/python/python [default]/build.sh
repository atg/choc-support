#!/bin/bash

VERB="Building"

# Helpers shared by all of Python's build scripts go in here.
source common.sh

if [[ "x$CHOC_BUILD" -ne "x" ]]; then
    echo -e ">>> Running custom script.\n"
    echo "$CHOC_BUILD" > $CHOC_TEMPFILE_1
    exec $CHOC_TEMPFILE_1
fi

[[ $SETUP = '' ]] && echo -e "Can not build without a setup.py script!" && exit 1

echo -e ">>> Running:\n>>>\tpython $SETUP build sdist bdist_egg\n"
python $SETUP build sdist bdist_egg > /dev/null

[[ $? -eq 0 ]] && echo ">>> Build successful!" || echo ">>> Build failed!"
