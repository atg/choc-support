# Chocolat Building Glue

The goal of this repo is to collect shell scripts that take a source file as input, and pass it through a compiler/interpreter/linter/etc.

We're on `##chocolatapp` on [irc.freenode.net](http://webchat.freenode.net/?channels=%23%23chocolatapp) if you want to help out.

The file TODO.txt contains the status of all languages we could think of (though it isn't exhaustive).

## Script Types

The project is organized as `<language>/<implementation>/<script>.sh`. We take a wide view on what an "implementation" is: if two tools are likely to be installed together and don't have conflicting scripts, we consider that the same "implementation". For instance: `ruby` and `irb` are part of the implementation "ruby", but `clang` and `gcc` come under their own implementations. In cases where multiple implementations are provided for, the most common should be tagged `[default]`.

There are a limited number of allowed script names:

* **run.sh** should run the file found in the environment variable `$CHOC_FILE`.
* **repl.sh** should load the file found in the environment variable `$CHOC_FILE` into a repl.
* **check.sh** should should perform syntactic (and optionally semantic) checking on the *standard input* passed to it (it's important that it uses *standard input* if possible and not `$CHOC_FILE` since we want to be able to check as the user is typing).
* **build.sh** should build the file found in the environment variable `$CHOC_FILE` and put its result into `$CHOC_BUILD_DIR`.
* **debug.sh** should run the file found in the environment variable `$CHOC_FILE` under an interactive debugger.

If you have ideas for more scripts, please let us know.

## The .chocbuild file

The optional `.chocbuild` directory lives in the project's directory and/or user's home directory. It provides alternative scripts to use when building. For instance, you can pick a different script for javascript with

    $ cat ~/.chocbuild/javascript/run.sh
    rhino "$CHOC_FILE"

Note the lack of an implementation directory. It's just `.chocbuild/<language>/<action>.sh`.

## Environment Variables

A few environment variables are provided to scripts:

    $CHOC_BUILD_DIR  # Where to put build products. Defaults to "build"
    
    $CHOC_FILE           # The path to the file
    $CHOC_FILENAME       # The name of the file
    $CHOC_EXT            # The file's extension
    $CHOC_FILENAME_NOEXT # The name of the file with the extension removed
    
    $CHOC_BUILD_DESTINATION # If the build product is only one file, this provides a suggestion for its path. Defaults to $CHOC_BUILD_DIR/$CHOC_FILENAME_NOEXT
    
    $CHOC_FILE_DIR       # The directory that contains the file
    $CHOC_PROJECT_DIR    # THe directory of the base project (may not be the same as $CHOC_FILE_DIR)
    
    $CHOC_TEMPFILE_1     # A path to a temporary file in which you can (please don't use mktemp since it uses the wrong location). The file will be deleted after the script exits.
    $CHOC_TEMPFILE_2
    $CHOC_TEMPFILE_3
