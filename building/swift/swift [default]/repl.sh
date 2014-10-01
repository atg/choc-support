cd "$CHOC_RUN_DIRECTORY" && xcrun swift -sdk $(xcrun --show-sdk-path --sdk macosx) -repl "$CHOC_FILE"
