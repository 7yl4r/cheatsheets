helpful links:
* [official redhat cheetsheet](https://access.redhat.com/sites/default/files/attachments/rh_yum_cheatsheet_1214_jcs_print-1.pdf)

## installations & software config
```
## === updates & installs
# update everything (and rm obsoletes)
sudo yum upgrade

# add an rpm from url
sudo rpm -Uvh https://yum.puppetlabs.com/puppet-release-el-8.noarch.rpm

# config alternatives (puppet at level 3 (higher takes precedence)
sudo alternatives --install /usr/bin/puppet puppet /opt/puppetlabs/bin/puppet 3

## === uninstalls & cleanups
# find an rpm package
rpm -qa | grep Micro_Focus

# uninstall an rpm package by name
rpm -e [package name]

# === cool yum-utils stuff 
# Find which repository a package comes from
find-repos-of-install

# Find processes that have been updated and need to restart
needs-restarting

# List installed RPM packages and statistics
show-installed

# Check the local yum repository for consistency
verifytree

# Try to complete yum transactions that didn’t finish
yum-complete-transaction
```
