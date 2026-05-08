from unittest import TestCase
from mock import patch

from parameterized import parameterized
import digits


class TestDigits(TestCase):

    @parameterized.expand([
        ("0", 0),
        ("1", 1),
        ("2", 2),
        ("10", 1),
        ("321", 6),
        ("1234567890", 45),
    ])
    @patch('builtins.input')
    def test_main(self, num, expected, input_mock):
        input_mock.return_value = num
        with patch('builtins.print') as print_mock:
            digits.main()
            print_mock.assert_called_with(expected)
