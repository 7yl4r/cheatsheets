#!/usr/bin/env python
""" boilerplate for new project setup.py """

from setuptools import setup
import io

VERSION = '0.0.1'  # should match __version__ in PROJECT_NAME.__init__.py


# === long_description comes from README.md
def read(*filenames, **kwargs):
    """Helper fn to help get project info for setup()"""
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')  # , 'CHANGELOG.md')

# === installation requirements read from requirements files
# so these two commands are equivalent:
# * `pip install .`
# * `pip install -r requirements.txt`
_tests_require = [
    line.strip() for line in open('tests_requirements.txt')
    if line.strip() and not line.strip().startswith('--')
]

_install_requires = [
    line.strip() for line in open('requirements.txt')
    if line.strip() and not line.strip().startswith('--')
]

_extras_require = {  # allows install w/ `pip install .[test]`
    'test': _tests_require
}
    
setup(
    name='projectname',
    description='short desc of projectname',
    url='https://github.com/7yl4r/projectname',
    entry_points={  # sets up CLI (eg bash) commands
        'console_scripts': [
            'projectname_cmd_name = projectname.import.path.to.my.cmd:method_name_in_that_module',
        ],
    },
    #cmdclass={'test': PyTest},  # custom build commands for test/lint/etc
    packages=[  # modules that are added to python when this is installed
        'projectname', 
        'OtherProjectProvidedPackage2'
    ],
    author_email='code+projectname@tylar.info',
    
    # === no edits needed past here
    author='Tylar Murray',
    version=VERSION,
    long_description=long_description,
    install_requires=_install_requires,
    tests_require=_tests_require,
    extras_require=_extras_require, 
)
