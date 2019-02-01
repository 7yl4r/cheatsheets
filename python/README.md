## snippets
snippets you might copy & paste often

```python
# format strings
# docs: https://docs.python.org/3/library/string.html#format-specification-mini-language
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
```

## reference
general reference links

* [list of built-in exceptions](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
* [list of strptime/strftime format string directives](http://strftime.org/)
* [regex cheatsheet](https://www.debuggex.com/cheatsheet/regex/python) & [debugger](https://www.debuggex.com/?flavor=python)
* [python format string reference](https://pyformat.info/)

### File i/o
* [xml via xml.etree.elementtree](https://docs.python.org/2/library/xml.etree.elementtree.html)

## reading
longer-form reading material:

* [book of python anti-patterns](http://docs.quantifiedcode.com/python-anti-patterns/)
