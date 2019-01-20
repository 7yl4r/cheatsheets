import logging

class ExampleClass(ParentClass):
    """ example class 
        This example class uses numpy-style docstrings.
            * style guide: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
            * detailed example: https://github.com/numpy/numpy/blob/master/doc/example.py
    """
    static_attr = "123abc"
    def __init__(self, param):
        """Summary line.

        Extended description of function.

        Parameters
        ----------
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2

        Returns
        -------
        bool
            Description of return value

        See Also
        --------
        otherfunc : some related other function

        Examples
        --------
        These are written in doctest format, and should illustrate how to
        use the function.

        >>> a=[1,2,3]
        >>> print [x + 3 for x in a]
        [4, 5, 6]
        """
        self.param = param
        self.logger = logging.getLogger(__name__)
    def method(self):
        self.stuff()
    @staticmethod
    def other_method():
        print("I can't access self but can be called without instantiation.")
    # === name mangling examples:
    def _protected_method(self):
        self.stuff()
    def __private_method(self):
        self.stuff()
    
