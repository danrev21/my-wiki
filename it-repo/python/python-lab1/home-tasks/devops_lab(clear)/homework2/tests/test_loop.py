from unittest import TestCase
from mock import patch

from parameterized import parameterized
import loop


class TestLoop(TestCase):

    @parameterized.expand([
        ("0", 1),
        ("1", 1),
        ("2", 2),
        ("3", 6),
        ("5", 120),
    ])
    @patch('builtins.input')
    def test_main(self, num, expected, input_mock):
        input_mock.return_value = num
        with patch('builtins.print') as print_mock:
            loop.main()
            print_mock.assert_called_with(expected)
