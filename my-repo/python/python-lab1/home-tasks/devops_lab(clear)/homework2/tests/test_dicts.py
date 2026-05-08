from unittest import TestCase
from mock import patch

from parameterized import parameterized
import dicts


class TestDict(TestCase):

    @parameterized.expand([
        ('{"c1": "Red", "c2": "Green", "c3": null}', {"c1": "Red", "c2": "Green"}),
        ('{}', {}),
        ('{"0": null, "1": "2"}', {"1": "2"}),
        ('{"test": null}', {}),
    ])
    @patch('builtins.input')
    def test_main(self, dictionary, expected, input_mock):
        input_mock.return_value = dictionary
        with patch('builtins.print') as print_mock:
            dicts.main()
            print_mock.assert_called_with(expected)
