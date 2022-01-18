# std modules:
from unittest import TestCase

# tested module(s):
from ExampleClass import ExampleClass

class Test_ExampleClass(TestCase):

    # === tests ============================================================
    def test_calls_my_method(self):
        """ thing1 and thing2 are equal """
        self.assertEqual('thing1', 'thing2')
        
