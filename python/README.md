## snippets
snippets you might copy & paste often

```bash
# run tests without a "real_db" mark:
python -m pytest -m "not real_db"
```

```python
# format strings
# docs: https://docs.python.org/3/library/string.html#format-specification-mini-language
# format type table: https://docs.python.org/2.4/lib/typesseq-strings.html
"""
format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""
'{:05.2f}'.format(3.1415)  # 03.14
'{:+1.0E}'.format(3.1415)  # +3E+00
# more examples @ pyformat.info

# breakpoints 
import pdb; pdb.set_trace()

# logging
import logging, sys
logger = logging.getLogger("{}.{}".format(
    __name__,
    sys._getframe().f_code.co_name)
)
logger.debug('lowest')  # -vvv only
logger.info('lower')    # -vv & above
logger.warn('middle')   # -v & above
logger.error('higher')
logger.critical('highest')

# ISO8601 strftime strings (b/c wtf datetime.isoformat()?)
ISO_8601_FMT = "%Y-%m-%dT%H:%M:%S.%f"
ISO_8601_SPACEY_FMT = ISO_8601_FMT.replace("T", " ")

# pretty print 
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint([[1,2,3],['a','b','c']])

# regex
import re
re.compile(".*").match("my_string")

# system calls & subprocesses
import subprocess
subprocess.run(['ls', '-lah', '~/'])

# add info to a caught exception
try:
    # yada yada...
except Exception as er:
    import sys
    raise (
        type(er), type(er)(
            e.message +
            '\n ADD YOUR INFO HERE'
        ), sys.exc_info()[2]
    )
```

## reference
general reference links

* [list of built-in exceptions](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
* [list of strptime/strftime format string directives](http://strftime.org/)
* [regex cheatsheet](https://www.debuggex.com/cheatsheet/regex/python) & [debugger](https://www.debuggex.com/?flavor=python)
* [python format string reference](https://pyformat.info/)

### File i/o
* [ensure dir exists](https://stackoverflow.com/questions/2793789/create-destination-path-for-shutil-copy-files/49615070#49615070): `os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)`
* [xml via xml.etree.elementtree](https://docs.python.org/2/library/xml.etree.elementtree.html)
* csv, tsv file handling via [pandas read_csv & write_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
* excel files via [pandas `read_excel`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)
```python
# === file paths, extensions, basenames, dirs
import os.path
abs_path = os.path.abspath("./file.txt")  # /abs/path/file.txt
fbase = os.path.basename("./test/file.txt")  # file.txt
path_str = os.path.join("dir", "subdir", "file.txt")  # dir/subdir/file.txt
basepath, ext = os.path.splitext("./test/file.txt")  # ./test/file, .txt
dirpath, fname = os.path.split("./dir/subdir/file.txt")  # ./dir/subdir/, file.txt

# === read raw text
with open(filepath, "r") as f_obj:
    for line in f_obj:
        print(line)
# === write raw text (append)
with open('action.csv', 'a') as f_obj:
    print('helloWorld', file=f_obj)
        
# TODO: add seek example(s)

# === temporary (tmp) files
import tempfile
print tempfile.gettempdir() # prints the current temporary directory

with tempfile.TemporaryFile() as tmpfile:
    tmpfile.write('something on temporaryfile')
```

## reading
longer-form reading material:

* [book of python anti-patterns](http://docs.quantifiedcode.com/python-anti-patterns/)
