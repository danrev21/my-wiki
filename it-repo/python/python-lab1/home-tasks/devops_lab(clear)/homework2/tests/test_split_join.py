from unittest import TestCase
from mock import patch

from parameterized import parameterized
try:
    import split_join
    SKIPPED = False
except ImportError:
    SKIPPED = True


class TestSplitJoin(TestCase):

    @parameterized.expand([
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        ("", ""),
        ("2", "2"),
        ("ab ba", "ba ab"),
    ])
    @patch('builtins.input')
    def test_main(self, num, expected, input_mock):
        if SKIPPED:
            return

        input_mock.return_value = num
        with patch('builtins.print') as print_mock:
            split_join.main()
            print_mock.assert_called_with(expected)
