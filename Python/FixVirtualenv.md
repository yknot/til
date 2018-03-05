# Fix Virtualenvs After Python Upgrade

When updating your version of python it can break your virtual environments. Using a script from [Github](https://gist.github.com/ttimasdf/34bc85ac008f68b2ee098850cab2979c#file-fix_virtualenv) you can just run 

```
workon virtualenv_name
fix_virtualenv
```

The full script is included below. It is pretty straightforward.

```
#!/usr/bin/env bash

# https://gist.github.com/ttimasdf/34bc85ac008f68b2ee098850cab2979c#file-fix_virtualenv
ENV_PATH="$(dirname "$(dirname "$(which pip)")")"
SYSTEM_VIRTUALENV="$(which -a virtualenv|tail -1)"

echo "Ensure the root of current virtualenv:"
echo "    $ENV_PATH"
read -p "‼️  Say no if you are not sure (y/N) " -n 1 -r
echo
PYEXC_DEF="$(sed -n '1s/^#!//p' $SYSTEM_VIRTUALENV)"
read -p "🐍  Choose which python to use? [$PYEXC_DEF] " PYEXC
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "♻️  Removing old symbolic links......"
    find "$ENV_PATH" -type l -delete -print
    echo "💫  Creating new symbolic links......"
    $SYSTEM_VIRTUALENV "$ENV_PATH" -p ${PYEXC:-$PYEXC_DEF}
    echo "🎉  Done!"
fi
```


