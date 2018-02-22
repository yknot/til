# Fix Jedi After Updating Homebrew Python

When updating your version of python it can break the links that jedi uses for things like emacs. To update them run these commands.

```
cd ~/.emacs.d/.python-environments
rm -rf default
virtualenv -p $(which python3) default
```

This might also need to be done for other python virtual environments on your system.
