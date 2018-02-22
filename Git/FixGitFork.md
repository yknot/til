# Fix a Git Fork with Messed Up History

First save all of your local changes somewhere just to make sure you don't blow them away. Then force push the right commit from the original repo to master. 

```git push origin +<hash>:master```

Then force pull to replace local.

```git reset --hard origin/master```

Finally reset your upstream commits.

```git merge upstream/master```
