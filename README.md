# Links
* [data viz catalogue](https://datavizcatalogue.com/)

# *nix
## piping & redirection
```
# pipe stderr & stdin to file
echo texthere &> myfile.txt

# redirect STDERR (2) to STDOUT (1) from docker logs, pipe to grep regex
docker logs erddap 2>&1 | grep -E "WARN|ERR"

# tee to print and save log to file
cmd | tee filename.log
```
## archives
### common `.tar.gz` tarball
* `tar -xvf archive.tar.gz` : `e`xtract `v`erbose `f`ilename

### high-compression (xz)
* `.xz` compress: `tar -cvJf file.tar.xz files/`
* `.xz` extract: `tar -xvf file.tar.xz`

### tar flag summary:
* `-x` extract
* `-v` verbose
* `-f` filename
* `-c` compress
* `-J` xz

## http downloads
```
# download file
curl http://example.com --output my.file
```

## rsync
Basic usage is usually `-azvh`:
```
    -a --archive
    -z --compress
    -v --verbose
    -h --human_readable
```

## grep
search without `-v` and use regex `-E`:
```
grep -Ev "word1|word2" example.txt
```

Examples
```bash
# For directory merging. Keeps most-recently modified version of files. 
rsync -habviuzP $OLDLOC/ $NEWLOC`  

# Sending to a remote server (eg USF supercomputer CIRCE)
rsync -azvh *-M1BS-* tylarmurray@circe.rc.usf.edu:/work/t/tylarmurray/img/Jobos/
```

## ssh
```
# generate new ssh id for your local user account
ssh-keygen -t ed25519 -C "email@tylar.info"  # NOTE: use default names & no pw otherwise you may need to configure w/ ssh-agent

# install ssh key on a remote server
ssh-copy-id -i ~/.ssh/id_rsa.pub user@server1.marine.usf.edu

```

## networking


### test connection to port
```
# use telnet
[root@seashell ~]# telnet 35.211.139.69 7070
Trying 35.211.139.69...
Connected to 35.211.139.69.
Escape character is '^]'.
^CConnection closed by foreign host.

# use netcat to test tcp
[root@seashell ~]# nc -z -v 35.211.139.69 7070
Connection to 35.211.139.69 7070 port [tcp/arcp] succeeded!

# use netcat to test udp
[root@seashell ~]# nc -z -v -u 35.211.139.69 7070
Connection to 35.211.139.69 7070 port [udp/arcp] succeeded!
```

## disks
```
# view disk config
lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINT
```

### partition + format
```
# === partition
gdisk /dev/$DISK
# p : show partitions 
# n : new
#    p : primary
# w : write and exit

# === fs setup
/sbin/mkfs.ext4 /dev/$DISK  # create file system on new partition
mount /dev/$DISK /loc/to/mount/to`  # temp test mount
vi /etc/fstab  
# && and add a line like:
# /dev/$DISK  /loc/to/mount/to   ext4    defaults    0   0`
```

* [fstab info](https://help.ubuntu.com/community/Fstab)

## accounts
```bash
groupadd -g 4747 grpname

useradd -d /home/ty -u 4747 -g 4747 -G sudo,admin,common -e 2999-12-30 ty
useradd -M nohomeuser

# add user to a group
usermod -a -G grpname username

# delete user
userdel username
```

## permissions
```bash
# set group permissions same as user
chmod -R g=u /location

# show permissions of full directory tree
namei -mo /home/user/dir/child/file
```

## clipboard-to-files
```bash
# see possible targets
xclip -selection clipboard -t TARGETS -o
# example to create image from clipboard
xclip -selection clipboard -t image/png -o > /tmp/myimage.png
```

## find
```bash
# exec
find . -exec grep chrome {} \;
# exec w/ pipe
find /path/to/jpgs -type f -exec sh -c 'jhead -v {} | grep 123' \;
# w/ xargs & command substitution
find ./content -type f -name 'DESCRIPTION' -print0 | \
    xargs -0 Rscript -e "devtools::install( \"$(sed -r 's|/[^/]+$||')\")"
```

## Space-saving Tips
```
# inspect the size of files in a directory
du -sh ./my_directory/*

# search for big files (example shows >5G)
find ./ -type f -size +5G

# search for unused files (example unaccessed for >90 days)
find ./ -type f -atime +90

# find content-identical files of size >10MB
jdupes -r -S -X size-:10M ./my_dir/
```

## FTP
```
lftp -c mirror ftp://ftp.nodc.noaa.gov/nodc/archive/arc0139/0190272/1.1/data/0-data/Sargassum_areal_coverage/
lftp 7yl4r@userftp.pgc.umn.edu:/3864_2019jul29> mirror --use-pget-n=4 .
```

# Text Editing
```
# find & replace text
sed 's/word1/word2/g' input.file > output.file
```

## vi
```
# delete all lines with given ending:
:g/_the_ending\.txt$/d
```

## system info
```
# distro info
cat /etc/*elease
```

## one-time setup stuff
```
# set my `history` cmd preferences:
echo 'export HISTTIMEFORMAT="%y-%m-%d %T "' >> ~/.bash_profile
echo 'export HISTCONTROL=ignoreboth:erasedups ' >> ~/.bash_profile
echo 'export HISTSIZE=100000 ' >> ~/.bash_profile
echo 'export HISTFILESIZE=10000000 ' >> ~/.bash_profile

```
