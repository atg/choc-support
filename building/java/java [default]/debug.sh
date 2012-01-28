bash build.sh #build prior to debugging
cd "$CHOC_BUILD_DIR" #cd to where it was built
jdb "$CHOC_FILENAME_NOEXT" #this assumes the file you want ran is the same as the file you just built

