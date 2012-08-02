#!/bin/bash

VERB="Testing"

# Helpers shared by all of Python's build scripts go in here.
source common.sh

if [[ "x$CHOC_TEST" -ne "x" ]]; then
    echo -e ">>> Running custom script.\n"
    echo "$CHOC_TEST" > $CHOC_TEMPFILE_1
    exec $CHOC_TEMPFILE_1
fi

# We prefer to run unit test suites if possible:
[[ $SETUP != '' ]] && echo -e ">>> Running unit test suite:\n>>>\tpython $SETUP test\n" && python $SETUP test && exit $? || exit $?

# Pass the modified source along to Python and test for everything.
[[ $SETUP != '' ]] || echo -e ">>> Passing script through parser.\n" && echo "raise SystemExit(); $(cat $CHOC_FILE)" | python -d -tt - && exit $? || exit $?
