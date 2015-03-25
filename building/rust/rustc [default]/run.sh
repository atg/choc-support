if [ -f "$CHOC_FILE_DIR/Cargo.toml"] then
    cd "$CHOC_FILE_DIR" && cargo run
elif [ -f "$CHOC_PROJECT_DIR/Cargo.toml"] then
    cd "$CHOC_PROJECT_DIR" && cargo run
else
    bash build.sh && cd "$CHOC_RUN_DIRECTORY" && exec "$CHOC_BUILD_DESTINATION"
fi
