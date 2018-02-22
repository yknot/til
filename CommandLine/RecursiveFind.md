# Recursive Find in Files

Find a string in a files named `file.txt` recursively checking, but avoiding pattern `SUBDIR` and look for `PATTERN` in those files.

```find . -name "file.txt" -not -path "./*/SUBDIR/*" | xargs grep "PATTERN" -A 5```


This just shows the power of the `find` command. While this case is pretty specific you can adapt different cases from it.

