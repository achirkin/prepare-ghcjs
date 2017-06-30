## Just let me make fresh GHCJS-stack source snapshot!

 1. Clone the repository
 2. Go into ghci within the project folder:
    `stack repl`
 3. Enable `OverloadedStrings` extension:
    `:set -XOverloadedStrings`
 4. Configure a desired lts-8.X snapshot, i.e.:
    `sync (lts8Cfg {checkResolver = return "lts-8.21"})`

The package should be available in folder `archive`.
Under the hood, this script downloads the latest snapshot of ghcjs from [ghcjs.luite.com](http://ghcjs.luite.com/).

# prepare-ghcjs

It is currently "designed" for one user.

I compile it and run via cron.
But the minimal will be:
clone

```
    stack ghci
    syncLts
    latest lts
    syncNightly
    latest nightly
    sync (ltsCfg {checkResolver = return "bla-123.456"})
    for resolver bla-123.456
```

the output should be in the archive.

This is very manual, In the ideal world all changes here should go to `ghcjs/ghcjs` or to upstream packages
I upload my builds thus I have `ghcjs-host` entry in `~/.ssh/config`

I still explore the design space. The operation on boot packages should be:

```
override_by_copy
copy_from_hackage
copy_from_boot
patch_hackage
```

some of them might generate new dependencies in `boot.yaml`


