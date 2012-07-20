#!/bin/bash

SYSTEM_PYTHON=$(which python)

if [[ "x$CHOC_PROJECT_DIR" != "x" ]]; then
    echo -e ">>> Project in:\n>>>\t$CHOC_PROJECT_DIR"
    echo -e ">>> File in:\n>>>\t$CHOC_FILE_DIR"

    cd "$CHOC_FILE_DIR"

    # Determine if we're within a full Python package.
    if [[ -f setup.py ]]; then
        SETUP="$PWD/setup.py"
    else
        while [[ "$PWD" != "$CHOC_PROJECT_DIR" ]]; do
            cd .. || break

            if [[ -f setup.py ]]; then
                SETUP="$PWD/setup.py"
                break
            fi
        done
    fi

    cd "$CHOC_FILE_DIR"

    # Activate a virtual environment if we can find it.
    if [[ -f bin/activate ]]; then
        source bin/activate
    else
        while [[ "$PWD" != "$CHOC_PROJECT_DIR" ]]; do
            cd .. || break
            if [[ -f bin/activate ]]; then
                echo -e ">>> Activating virtual environment:\n>>>\t$PWD/bin/activate"
                source bin/activate
                break
            fi
        done
    fi

    cd "$CHOC_PROJECT_DIR"

    if [[ "x$VIRTUAL_ENV" == 'x' && -e "bin" ]]; then
        echo ">>> Adding project bin folder to path."
        export PATH="$CHOC_PROJECT_DIR/bin:$PATH"
    fi
fi

# Emit some potentially useful information about the Python we're checking against.
echo -e ">>> $VERB against $(python -V 2>&1) from:\n>>>\t$(which python)"

[[ "x$SETUP" != "x" && "x$VIRTUAL_ENV" != 'x' ]] && echo -e ">>> Registering package with virtualenv:\n>>>\tpython $SETUP develop" && python $SETUP develop > /dev/null
