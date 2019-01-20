#!/usr/bin/env python
""" boilerplate for new project setup.py """

from setuptools import setup
import io

import projectname

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md') #, 'CHANGES.txt')

setup(name='projectname',
    version=projectname.__version__,
    description='short desc of projectname',
    long_description=long_description,
    author='Tylar Murray',
    author_email='code+projectname@tylar.info',
    url='https://github.com/7yl4r/projectname',

    tests_require=['nose'],
    install_requires=[
        'networkx'  # or whatever
    ],
    entry_points={  # sets up CLI (eg bash) commands
        'console_scripts': [
            'projectname_cmd_name = projectname.import.path.to.my.cmd:method_name_in_that_module',
        ],
    },
    #cmdclass={'test': PyTest},  # custom build commands for test/lint/etc
    packages=[  # modules that are added to python when this is installed
        'projectname', 
        'OtherProjectProvidedPackage2'
    ]
)
