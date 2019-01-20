"""
example unit test for ExampleClass

list of unittest assert methods: https://docs.python.org/3/library/unittest.html#assert-methods
"""

# std modules:
from unittest import TestCase
try:
    # py2
    from mock import MagicMock
except ImportError:
    # py3
    from unittest.mock import MagicMock

class Test_ExampleClass_main(TestCase):

    # tests:
    #########################
    @patch('ExampleClass.my_method')  # monkey patch to collect info on calls instead of actually calling
    def test_calls_my_method(self, mock_my_method):
        """ ExampleClass module calls my_method twice """
        with patch('os.walk') as mock_walk:  # another syntax for monkey patching
         
            # tested module(s):
            from ExampleClass import ExampleClass
            # NOTE: you must import AFTER monkey patching!!!

            mock_walk.return_value = [
                '/home/username/my_folder', 
                ('my_subfolder', 'my_other_subdir'),
                ('file_in_my_folder.csv', 'files_in_subfolders_not_here_though.md')
            ]
        
            # parse_args is argv[] parsing function (see `projectname_main.py`)
            test_args = parse_args([  
                '-vv',
                'subcommand',
                '--subcommand_arg',
                '-k', 'my_key_val_arg_value',
            ])
            result = ExampleClass.stuff(test_args)
        
        self.assertEqual(mock_my_method.call_count, 2)
        
        # === other useful test patterns:
        # multiple values expected in result array:
        self.assertTrue(('yada', 'whatever') in result)
        self.assertDictContainsSubset(
            {
                "my_key" : "my_value"
            },
            my_dict_containing_at_least_key_vals_in_dict_above
        )

        with self.assertRaises(TypeError):
            something_that_raises_type_err(2)
