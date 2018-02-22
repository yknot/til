# Check for Rootless and Gatekeeper

How to check the status and disable these two features. Not that I recommend doing either unless you know what you are doing, but just in case you want to.

Check for rootless mode

```csrutil status```

Disable rootless

```sudo csrutil disable```

Check gatekeeper status

```spctl --status```

Disable gatekeeper

```sudo spctl --master-disable```
