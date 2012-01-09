# Chocolat Code Completion Support

*We're on `##chocolatapp` on [irc.freenode.net](http://webchat.freenode.net/?channels=%23%23chocolatapp) if you want to help out.*

There's three prongs to Chocolat's code completion:

1. Word completion: words that are found in the current document. This happens when you press `esc`.
2. Indexed completions: symbols that are found in the current document or project. This is provided by [diglett](http://github.com/fileability/diglett).
3. **Static completions:** completions that are *not* found in the current document or project. What this repo is all about.

Static completions are things like CSS properties, standard library function names, etc. Things that could appear in Chocolat's code completion menu, but can't be indexed out of the document/project by diglett.

Here's how it works:

### Structure

Each language gets its own directory (the name of the directory is a scope). Each directory contains one or more .json files for each separate group of completions (eg `js/functions.json`, `js/constants.json`).

### JSON format

Each JSON file is an object literal, with the following keys:
    
    [required]
    items: An array of strings corresponding
    
    [optional]
    selector: A scope selector 
    type: function/class/type/method/constant/etc
    icon: usually the same as 'type'
    prototypes: A parallel array of prototype declarations. If 'prototypes' is given, there must be one value in the array for each value in 'items'.

### Compiling

A script, `compile.py` runs all the scripts, then takes all the JSON files and compiles them into 1 monolithic completions.json file to be used by Chocolat.
