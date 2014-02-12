#!/bin/bash

mkdir -p "$CHOC_BUILD_DIR" && go build -o "$CHOC_BUILD_DIR/$CHOC_FILENAME_NOEXT" "$CHOC_FILE"
