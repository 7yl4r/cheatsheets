"""
example unit test for ExampleClass

list of unittest assert methods:
https://docs.python.org/3/library/unittest.html#assert-methods
"""

# std modules:
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import MagicMock

# tested module(s):
from ExampleClass import ExampleClass


class Test_ExampleClass_main(TestCase):

    # tests:
    #########################
    @patch('os.stat')  # patch to collect info instead of actually calling
    def test_calls_my_method(self, mock_os_stat):
        """ ExampleClass module calls my_method twice """
        with patch('os.walk') as mock_walk:  # alt syntax for monkey patching

            mock_walk.return_value = [
                '/home/username/my_folder',
                ('my_subfolder', 'my_other_subdir'),
                ('file_in_my_folder.csv', 'files_in_subdirs_not_here_tho.md')
            ]

            # new return value for each call w/ side_effect:
            mock_os_stat.side_effect = [
                MagicMock(st_mode=11111, st_ino=11111111, st_dev=2049),
                MagicMock(st_mode=22222, st_ino=22222222, st_dev=2049),
            ]

            eg_class_obj = ExampleClass()
            # replace class method with MagicMock
            eg_class_obj.class_method = MagicMock(
                name='class_method',
                side_effect=[1, 2, 3],
                return_value=0
            )
            ExampleClass.other_class_method()

            # expect class_method was called twice by other_class_method()
            self.assertEqual(eg_class_obj.class_method.call_count, 2)

        # === other useful test patterns:
        # multiple values expected in result array:
        self.assertTrue(('yada', 'whatever') in result)
        self.assertDictContainsSubset(
            {
                "my_key": "my_value"
            },
            my_dict_containing_at_least_key_vals_in_dict_above
        )

        with self.assertRaises(TypeError):
            something_that_raises_type_err(2)
