cd "$CHOC_PROJECT_DIR"
version=`cat $CHOC_FILE || grep 'use v6;'`
if [ -n "$version" ]; then
	perl6 "$CHOC_FILE"
else
	perl "$CHOC_FILE"
fi
