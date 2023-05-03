## rebase-based multibranch workflow
When maintaining multiple branches rebasing off of the master [eg](https://github.com/USF-IMARS/erddap-config), it is sometimes useful to create a backup branch
```bash
# del extant *-backup branch & update origin w/ latest 
BRANCH=dune
git checkout $BRANCH && git branch -D $BRANCH-backup && git branch $BRANCH-backup && git checkout $BRANCH-backup && git push -f origin $BRANCH-backup && git checkout $BRANCH && git branch -D $BRANCH-backup
```

## Log Graph Visual
```
# git "network" view (remember `git log "A DOG"`)
git log --all --decorate --oneline --graph
```

## Submodules 

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

## .gitignore
Ignore everything inside this folder but keep the folder by adding a `.gitignore` with content :

:warning: you can also do this with a `.gitkeep` file.

```
# Ignore everything in this directory
*
# Except this file
!.gitignore
```
