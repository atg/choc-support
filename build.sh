#!/bin/bash

# Find and compile any coffeescript files
find . -name '*.coffee' | xargs coffee -b -c

# Run the json compilation scripts
cd docs && python compile.py && cd ..
cd completions && python compile.py && cd ..
cd SPLDB && python compiler.py && cd ..

cd extended-completions && python parseattributes.py >html.min.json && cd ..
cd extended-completions && python cssgen.py >css.min.json && cd ..
