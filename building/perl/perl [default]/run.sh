cd "$CHOC_RUN_DIRECTORY"
version=`cat $CHOC_FILE || grep 'use v6;'`
if [ -n "$version" ]; then
	perl6 "$CHOC_FILE"
else
	perl "$CHOC_FILE"
fi
