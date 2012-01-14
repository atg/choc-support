# SPLDB: Semantic Programming Language Database

**SPLDB** is a project to build a database of programming language metadata (info, conventions, syntax, semantics, etc) in a form that computers can consume.

## Why?

In [Chocolat](http://chocolatapp.com) (a text editor for Mac), we have a class which stores information about various programming languages. But hardcoded objects in source aren't ideal. If we want to update the data, we have to change the source and ship a new update. And others can't easily contribute new languages.

**SPLDB** is intended for anyone who needs to analyze, modify or edit source code.

## Setup

**SPLDB** is developed as a series of json files, one file per language. The `compile.py` script takes these json files then assembles and minifies them into one big file called `data.json`.

To get started:

    git clone https://github.com/fileability/SPLDB.git
    python compiler.py
    cat data.json

Then use one of the many [JSON implementations](http://www.json.org/).

## Contributing

Please submit any changes as a pull request.

### Extending Languages

The following keys are currently accepted for use:

    name (string):
        A display name for the language, complete with spaces and correct capitalization. This should be the *most common* rendering of the name.
    
    extensions (string|array):
        Filename extensions for _source_ files. `.o`, `.pyc`, etc don't count.
        For example:
            "extensions": ["cpp", "c++", "cxx", "cc"]
            "extensions": "py"
    
    tab-width (int):
        Consensus on tab size (in spaces), if it exists (eg 4 for python).
    soft-tabs (bool):
        Consensus on whether to use soft tabs or hard tabs, if it exists.
    
    comment.line (string|array):
        A string that starts a line comment
    comment.block.start (string|array):
        A string that starts a block comment. If array, must have same length as comment.block.end.
    comment.block.end (string|array):
        A string that ends a block comment. If array, must have same length as comment.block.start.
    comment.nested.start (string|array):
        A string that starts a nested block comment.
    comment.nested.end (string|array):
        A string that ends a nested block comment.


This is by no means all the keys we're ever going to have, so if you have an idea for a new key, please [submit an issue](/fileability/SPLDB/issues). You might want to have a look at [Hyperpolyglot](http://hyperpolyglot.org) which is the same sort of thing, but for humans instead of computers.

### New Languages

If you want to contribute a *new* language, create a file `languagename.json`. The file's name should be all lowercase, and contain no spaces (use hyphens instead). The file's name shouldn't be abbreviated unless the language's name is almost always abbreviated that way (`objective-c.json` but `ocaml.json`).

Then put in a bit of boilerplate:

    {
        "name": "OCaml",
    }

The `name` attribute is used to give a display name to the language, complete with spaces and correct capitalization. This should be the *most common* rendering of the name.

