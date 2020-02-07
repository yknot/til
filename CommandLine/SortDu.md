# Sorting Output

I always forget about commands like `sort` which are so useful for quick parsing of outputs of a file. Just used this for sorting output of `du` which is another great tool for quickly checking disk usage for a file or folder.

```sort -n -r -k 1```

- `-n` means treat values as numeric so you don't sort by ascii/alpha value
- `-r` means reverse which means descending for numbers
- `-k <n>` means sort by "field" or column `n`. If you don't do `1,1` it will sorty by the first field and until the end of the fields which might do weird things to break ties.
