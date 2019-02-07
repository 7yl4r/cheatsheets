# *nix
## archives
### high-compression (xz)
* `.xz` compress: `tar -cvJf file.tar.xz files/`
* `.xz` extract: `tar -xvf file.tar.xz`

## rsync
Basic usage is usually `-azvh`:
```
    -a --archive
    -z --compress
    -v --verbose
    -h --human_readable
```

Options for directory merging: `rsync -habviuzP $OLDLOC/ $NEWLOC`. This keeps the most-recently modified version of the file.
