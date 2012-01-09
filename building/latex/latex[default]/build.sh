# Should be $CHOC_BUILD_DIR but unfortunately it doesn't work

pdflatex -synctex=1 -output-directory="$CHOC_PROJECT_DIR" "$CHOC_FILE"
exit