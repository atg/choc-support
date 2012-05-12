cd $CHOC_FILE_DIR;

# By convention, AS3 builds to `bin/`
# But when in Rome, I guess:
mkdir -p "$CHOC_BUILD_DIR"; 

if [ ! mxmlc ]; then
	echo "Please add mxmlc to your $PATH"
	# Untested on other systems.
fi

# Thank you, Pini: http://bit.ly/w1VOPU
relativePath () {
	source=$1
	target=$2

	common_part=$source
	back=
	while [ "${target#$common_part}" = "${target}" ]; do
	  common_part=$(dirname $common_part)
	  back="../${back}"
	done

	echo ${back}${target#$common_part/}
}

BUILD_PATH=`relativePath $CHOC_FILE_DIR $CHOC_BUILD_DIR`;

mxmlc "$CHOC_FILE" -sp "$CHOC_FILE_DIR" -o "$BUILD_PATH/$CHOC_FILENAME_NOEXT.swf" -static-link-runtime-shared-libraries=true;