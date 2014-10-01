mkdir -p "$CHOC_BUILD_DIR"; xcrun swift -sdk $(xcrun --show-sdk-path --sdk macosx) -o "$CHOC_BUILD_DESTINATION" "$CHOC_FILE"
