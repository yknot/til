# Creating and Using SSH Keys

Here's an easy workflow to create and use ssh keys.


```ssh-keygen -t rsa```

Then follow the prompts naming the file. Finally copy the id (`.pub` file) over to the remote host.

```ssh-copy-id -i <key_file> username@host```
