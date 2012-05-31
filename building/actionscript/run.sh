# sh build.sh?

# vars
LOG=~/Library/Preferences/Macromedia/Flash\ Player/Logs/flashLog.txt;
MM=/Library/Application\ Support/Macromedia/mm.cfg;

# back up old mm.cfg (if exists)
if [ -f "$MM" ]; then
	mv "$MM" "$MM.bak";
fi

# create new mm.cfg
echo "ErrorReportingEnable=1" >> "$MM";
echo "TraceOutputFileEnable=1" >> "$MM";
echo "MaxWarnings=0" >> "$MM";

# Open Main.swf
open -a "Flash Player Debugger" "$CHOC_BUILD_DIR/$CHOC_FILENAME_NOEXT.swf"

# Live view output
tail -f "$LOG";

# NOTE: This needs to execute after Flash Player is closed.
# Right now it only executes once the `tail` is CTRL-C'd

# Delete new mm.cfg
rm "$MM";

# Put back old files (if exists)
if [ -f "$MM.bak" ]; then
	mv "$MM.bak" "$MM";
fi