from unittest import TestCase
from mock import patch

from parameterized import parameterized
import strings


class TestStrings(TestCase):

    @parameterized.expand([
        ("", "yes"),
        ("1", "yes"),
        ("abc", "no"),
        ("abcba", "yes"),
    ])
    @patch('builtins.input')
    def test_main(self, num, expected, input_mock):
        input_mock.return_value = num
        with patch('builtins.print') as print_mock:
            strings.main()
            print_mock.assert_called_with(expected)
