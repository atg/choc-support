#!/bin/bash

echo -e ">>> Project in:\n>>>\t$CHOC_PROJECT_DIR"
echo -e ">>> File in:\n>>>\t$CHOC_FILE_DIR"

SYSTEM_PYTHON=$(which python)

cd "$CHOC_FILE_DIR"

# Determine if we're within a full Python package.
# This would actually work if $CHOC_PROJECT_DIR didn't lie.
if [[ -f setup.py ]]; then
    SETUP="$PWD/setup.py"
else
    # while [[ "$PWD" != "$CHOC_PROJECT_DIR" ]]; do
    while [[ "$PWD" != "/" ]]; do
        cd .. || break
        
        if [[ -f setup.py ]]; then
            SETUP="$PWD/setup.py"
            break
        fi
    done
fi

cd "$CHOC_PROJECT_DIR"

# Activate a virtual environment if we can find it.
# Suffers the same CHOC_PROJECT_DIR issue as above.

if [[ -f bin/activate ]]; then
    source bin/activate
else
    # while [[ "$PWD" != "$CHOC_PROJECT_DIR" ]]; do
    while [[ "$PWD" != "/" ]]; do
        cd .. || break
        if [[ -f bin/activate ]]; then
            echo -e ">>> Activating virtual environment:\n>>>\t$PWD/bin/activate"
            source bin/activate
            break
        fi
    done
fi

cd "$CHOC_PROJECT_DIR"

#if [ -e "$CHOC_PROJECT_DIR/bin/activate" ]; then
#    echo -e ">>> Activating virtual environment."
#    source $CHOC_PROJECT_DIR/bin/activate
#elif [ -e "bin" ]; then
#    echo ">>> Adding project bin folder to path."
#    export PATH="$CHOC_PROJECT_DIR/bin:$PATH"
#fi

# Emit some potentially useful information about the Python we're checking against.
echo -e ">>> $VERB against $(python -V 2>&1) from:\n>>>\t$(which python)"

[[ $SETUP != '' && "x$VIRTUAL_ENV" != 'x' ]] && echo -e ">>> Registering package with virtualenv:\n>>>\tpython $SETUP develop" && python $SETUP develop > /dev/null
