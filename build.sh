#!/bin/bash

# Find and compile any coffeescript files
find . -name '*.coffee' | xargs coffee -b -c

# Run the json compilation scripts
cd docs && python compile.py && cd ..
cd completions && python compile.py && cd ..
cd SPLDB && python compiler.py && cd ..

