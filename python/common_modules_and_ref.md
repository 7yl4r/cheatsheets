## snippets
snippets you might copy & paste often

```python
# breakpoints 
import pdb
pdb.set_trace()

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

## reading
longer-form reading material:

* [book of python anti-patterns](http://docs.quantifiedcode.com/python-anti-patterns/)
