# try to figure out our chocolat app path if
# it wasn't passed in to us
if [[ ! $CHOC_APP_PATH && ${CHOC_APP_PATH-x} ]]; then
	CHOC_APP_PATH=$(/usr/bin/osascript <<-EOF
	tell application "System Events"
		if (get name of every process) contains "Chocolat" then
			tell application process "Chocolat"
				set a to application file
				POSIX path of a
			end tell
		end if
	end tell
	EOF)
fi

JSHINT_ASSET_DIR="$PWD"
JSHINT_DEFAULT_CONFIG=""

if [[ ! -e "$HOME/.jshintrc" && ! -e "$CHOC_PROJECT_DIR/.jshintrc" ]]; then
	JSHINT_DEFAULT_CONFIG="$JSHINT_ASSET_DIR/jshintrc"
fi

if [[ -e "$CHOC_APP_PATH" ]]; then
	#echo "cd \"$CHOC_PROJECT_DIR\" && \"$CHOC_APP_PATH/Contents/MacOS/Chocolat\" --pretend-node \"$JSHINT_ASSET_DIR/node_modules/.bin/jshint\" --reporter \"$JSHINT_ASSET_DIR/choc_reporter.js\" --config \"$JSHINT_DEFAULT_CONFIG\" \"$CHOC_FILE\""
	cd "$CHOC_PROJECT_DIR" && "$CHOC_APP_PATH/Contents/MacOS/Chocolat" --pretend-node "$JSHINT_ASSET_DIR/node_modules/.bin/jshint" --reporter "$JSHINT_ASSET_DIR/choc_reporter.js" --config "$JSHINT_DEFAULT_CONFIG" "$CHOC_FILE"
fi