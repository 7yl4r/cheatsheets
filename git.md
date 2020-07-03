
```bash
# initialize (if needed) & update all submodules
git submodule update --init --recursive --remote

# add a new submodule to track a branch (master)
git submodule add -b master https://github.com/un/repo_name.git src/path/to/module

# delete a submodule
git submodule deinit -f path/to/submodule
rm -rf .git/modules/path/to/submodule
git rm -f path/to/submodule
```
