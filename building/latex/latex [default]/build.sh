# Should be $CHOC_BUILD_DIR but unfortunately it doesn't work

mkdir -p "$CHOC_BUILD_DIR"; pdflatex -synctex=1 -output-directory="$CHOC_BUILD_DIR" "$CHOC_FILE"
exit