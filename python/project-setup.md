### generic project structure:
```
projectname/ # project root
    conf/         # config files, could also be put in projectname/projectname/
    lib/          # libraries, optional if you use a package manager like pip
    projectname/  # src
        __init__.py
        projectname.py  # py interface for projname?
        my_core_file_name.py
        submodule/
            __init__.py
            my_submodule_name.py
    setup.py              
    README.md
    LICENSE
    projectname.py  # CLI for projname (see projectname_main.py)
```

### setup checklist
1. .gitignore, README.md, LICENSE (use github for these usually)
2. set `__version__` in `projectname/__init__.py`
2. create setup.py
3. `pip install -e .`  (or pip3) from project root
