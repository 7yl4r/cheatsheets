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


## accounts
```
groupadd -g 4747 grpname

useradd -d /home/ty -u 4747 -g 4747 -G sudo,admin,common -e 2999-12-30 ty
useradd -M nohomeuser

usermod -a G grpname username
```

## permissions
```
# set group permissions same as user
chmod -R g=u /location
```
