if [ -f "$CHOC_FILE_DIR/Cargo.toml"] then
    cd "$CHOC_FILE_DIR" && cargo build
elif [ -f "$CHOC_PROJECT_DIR/Cargo.toml"] then
    cd "$CHOC_PROJECT_DIR" && cargo build
else
    mkdir -p "$CHOC_BUILD_DIR"; rustc -O -o "$CHOC_BUILD_DESTINATION" "$CHOC_FILE"
fi
