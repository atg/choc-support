mkdir -p "$CHOC_BUILD_DIR"; clang++ -std=c++11 -stdlib=libc++ -x c++ -Os -o "$CHOC_BUILD_DESTINATION" "$CHOC_FILE"
