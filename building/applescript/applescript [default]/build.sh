#!/bin/bash

osacompile -o "$CHOC_FILENAME_NOEXT.scpt" "$CHOC_FILE" && mkdir -p "$CHOC_BUILD_DIR" && mv "$CHOC_FILENAME_NOEXT.scpt" "$CHOC_BUILD_DIR"
