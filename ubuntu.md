# alternatives & symlinking bash completion stuff
```
# === install a symlink :
update-alternatives --install link            name   path                              priority
# examples:
update-alternatives --install /usr/bin/java   java   /usr/lib/jvm/jdk1.8.0.05/bin/java 10
update-alternatives --install /usr/bin/puppet puppet /opt/puppetlabs/bin/puppet        10
```

# debian packages
```
# list stuff
dpkg -l '*puppet*'  # list all packages matching the given glob
dpkg -L puppet-agent | grep -E '/s?bin/'  # list all files from a package, grep the result for likely binaries

# install/purge
dpkg -i puppet7-release-focal.deb  # install a .deb file
dpkg -P puppet  # purge (agrressive delete) a .deb by name (from `dpkg -l`)
```

# user setup
```bash
# add a new sudo user
adduser sammy_the_user
usermod -aG sudo sammy_the_user
```
