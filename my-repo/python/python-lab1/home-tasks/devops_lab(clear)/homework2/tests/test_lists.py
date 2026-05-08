from unittest import TestCase
from mock import patch, call
from parameterized import parameterized

import lists


class TestLists(TestCase):

    @parameterized.expand([
        (["10",
          "insert 0 5",
          "insert 1 10",
          "insert 0 6",
          "remove 6",
          "append 9",
          "append 1",
          "sort",
          "pop",
          "reverse",
          "print"],
         [call([9, 5, 1])]),
        (["0"],
         []),
        (["2",
          "append 1",
          "print"],
         [call([1])]),
        (["4",
          "append 3",
          "append 1",
          "sort",
          "print"],
         [call([1, 3])]),
    ])
    @patch('builtins.input')
    def test_main(self, commands, expected, input_mock):
        input_mock.side_effect = commands
        with patch('builtins.print') as print_mock:
            lists.main()
            print_mock.assert_has_calls(expected)
