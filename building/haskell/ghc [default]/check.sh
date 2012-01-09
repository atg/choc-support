#!/usr/bin/env bash

cat "$CHOC_TEMPFILE_1" && ghc -c "$CHOC_TEMPFILE_1" -o "$CHOC_TEMPFILE_2" -ohi "$CHOC_TEMPFILE_3"
