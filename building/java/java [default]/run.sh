bash build.sh #build prior to running
cd "$CHOC_PROJECT_DIR" #cd to where it was built
java "$CHOC_FILENAME_NOEXT" #this assumes the file you want ran is the same as the file you just built

