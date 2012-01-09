#!/usr/bin/env bash

ghc --make "$CHOC_FILE" -o "$CHOC_BUILD_DESTINATION" -hidir "$CHOC_BUILD_DIR" -odir "$CHOC_BUILD_DIR" -stubdir "$CHOC_BUILD_DIR" -outputdir "$CHOC_BUILD_DIR"
