#!/bin/bash

# Find and compile any coffeescript files
find . -name '*.coffee' | xargs coffee -b -c

# Run the json compilation scripts


