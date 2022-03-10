# recommended python package tooling (Pipfile + pipenv)
## Setting up a new package
1. add a Pipfile to your project (example [here](https://github.com/7yl4r/cheatsheets/blob/master/python/Pipfile))
2. include all dependencies in the Pipfile

## Installing a package from github w/ Pipfile
### pyenv + pipenv
```
# 1. install python + pip + pipenv
# 2. git clone the project, cd there, then do:
python -m pipenv install  # to install requirments from `Pipfile`
```

# other toolings 
## package installation (virtualenv + git)
1. git clone
2. set up virtualenv
3. pip install -e .

# Packaging for Production Deployments
This section is for the steps needed to get a package onto pypi.

*Options*:
1. distutils (rpm, windows, source)
    * [overview](https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications)
    * [docs](https://docs.python.org/2/distutils/builtdist.html)
2. dh-virtualenv (.deb)
    * [overview](https://www.nylas.com/blog/packaging-deploying-python/)

See also:
* [An aggravated historical reflection on python distribution tools](http://lucumr.pocoo.org/2012/6/22/hate-hate-hate-everywhere/).
