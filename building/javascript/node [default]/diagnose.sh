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

ASSET_DIR="$PWD"
JSHINT_DEFAULT_CONFIG="$ASSET_DIR/.jshintrc"
JSCS_DEFAULT_CONFIG="$ASSET_DIR/.jscsrc"

if [[ -e "$HOME/.jshintrc" ]]; then
	JSHINT_DEFAULT_CONFIG="$HOME/.jshintrc"
fi

if [[ -e "$CHOC_PROJECT_DIR/.jshintrc" ]]; then
	JSHINT_DEFAULT_CONFIG="$CHOC_PROJECT_DIR/.jshintrc"
fi

if [[ -e "$HOME/.jscsrc" ]]; then
	JSCS_DEFAULT_CONFIG="$HOME/.jscsrc"
fi

if [[ -e "$CHOC_PROJECT_DIR/.jscsrc" ]]; then
	JSCS_DEFAULT_CONFIG="$CHOC_PROJECT_DIR/.jscsrc"
fi

if [[ -e "$CHOC_APP_PATH" ]]; then
	# echo "cd \"$CHOC_PROJECT_DIR\" && \"$CHOC_APP_PATH/Contents/MacOS/Chocolat\" --pretend-node \"$ASSET_DIR/diagnose.js\" --jshint-config \"$JSHINT_DEFAULT_CONFIG\" --jscs-config \"$JSCS_DEFAULT_CONFIG\" \"$CHOC_FILE\"" >> ./log2
	cd "$CHOC_PROJECT_DIR" && "$CHOC_APP_PATH/Contents/MacOS/Chocolat" --pretend-node "$ASSET_DIR/diagnose.js" --jshint-config "$JSHINT_DEFAULT_CONFIG" --jscs-config "$JSCS_DEFAULT_CONFIG" "$CHOC_FILE"
fi