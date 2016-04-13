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

if [[ -e "$CHOC_APP_PATH" ]]; then
	cd "$CHOC_PROJECT_DIR" && HOME=$HOME CHOC_PROJECT_DIR=$CHOC_PROJECT_DIR CHOC_FILE=$CHOC_FILE CHOC_PROJECT_FILE=$CHOC_PROJECT_FILE "$CHOC_APP_PATH/Contents/MacOS/Chocolat" --pretend-node $PWD
fi