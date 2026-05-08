from unittest import TestCase
from mock import patch

from parameterized import parameterized
import sets


class TestDisct(TestCase):

    @parameterized.expand([
        (("1", "2"), []),
        (("", ""), []),
        (("2", "1 2"), [2]),
        (("2 1", "2 1"), [1, 2]),
        (("1 1 2 3 5 8 13 21 34 55 89", "1 2 3 4 5 6 7 8 9 10 11 12 13"), [1, 2, 3, 5, 8, 13]),
    ])
    @patch('builtins.input')
    def test_main(self, lists, expected, input_mock):
        input_mock.side_effect = lists
        with patch('builtins.print') as print_mock:
            sets.main()
            print_mock.assert_called_with(expected)
