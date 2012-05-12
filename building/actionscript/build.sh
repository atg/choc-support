# By convention, AS3 builds to `bin/`
# But when in Rome, I guess:
mkdir -p "$CHOC_BUILD_DIR"; 

cd $CHOC_BUILD_DIR;

if [ ! mxmlc ]; then
	echo "Please add mxmlc to your $PATH"
	# Untested on other systems.
fi

mxmlc "$CHOC_FILE" -sp "$CHOC_PROJECT_DIR/src" -o "$CHOC_FILENAME_NOEXT.swf" -static-link-runtime-shared-libraries=true;