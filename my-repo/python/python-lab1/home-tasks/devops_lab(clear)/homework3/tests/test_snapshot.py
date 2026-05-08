from collections import namedtuple
from freezegun import freeze_time
import json
from mock import patch
from random import randint
import tempfile
from unittest import TestCase

from snapshot import snapshot


class TestApple(TestCase):

    def _generate_iter(self):
        res = []
        for i in range(8):
            res.append(namedtuple('Iter', ["info", "status"])({"status": "running"},
                                                              lambda: "running"))

        for i in range(9):
            res.append(namedtuple('Iter', ["info", "status"])(
                {"status": "stopped"}, lambda: "stopped"))

        for i in range(10):
            res.append(namedtuple('Iter', ["info", "status"])(
                {"status": "sleeping"}, lambda: "sleeping"))

        for i in range(11):
            res.append(namedtuple('Iter', ["info", "status"])(
                {"status": "zombie"}, lambda: "zombie"))

        return res

    def _generate_process(self, i):
        if 1 <= i <= 8:
            return namedtuple('Process', ["status"])(lambda: "running")

        if 9 <= i <= 17:
            return namedtuple('Process', ["status"])(lambda: "stopped")

        if 18 <= i <= 27:
            return namedtuple('Process', ["status"])(lambda: "sleeping")

        return namedtuple('Process', ["status"])(lambda: "zombie")

    @patch('psutil.pids')
    @patch('psutil.Process')
    @patch('psutil.process_iter')
    @patch('psutil.cpu_times_percent')
    @patch('psutil.virtual_memory')
    @patch('psutil.swap_memory')
    @patch("argparse.ArgumentParser.parse_args")
    @patch('builtins.print')
    @patch('time.sleep')
    @freeze_time('2021-06-23 00:00:00Z')
    def test_snapshot(self, sleep_mock, print_mock, parse_mock, swap_mock,
                      virtual_mock, cpu_mock, iter_mock, process_mock, pids_mock, ):
        swaps = [randint(1, 10) for _ in range(3)]
        virtuals = [randint(1, 10) for _ in range(3)]
        cpus = [randint(1, 10) for _ in range(4)]
        expected = \
            {"Tasks": {"total": 38, "running": 8, "sleeping": 10, "stopped": 9, "zombie": 11},
             "%CPU": {"user": cpus[0], "system": cpus[2], "idle": cpus[3]},
             "KiB Mem": {"total": virtuals[0], "free": virtuals[1], "used": virtuals[2]},
             "KiB Swap": {"total": swaps[0], "free": swaps[1], "used": swaps[2]},
             "Timestamp": 1624406400}
        swap_mock.return_value = namedtuple('Swap', ["total", "free", "used"])(
            *(i * 1024 for i in swaps))
        virtual_mock.return_value = namedtuple('Virtual', ["total", "free", "used"])(
            *(i * 1024 for i in virtuals))
        iter_mock.return_value = self._generate_iter()
        cpu_mock.return_value = namedtuple('CPU', ["user", "nice", "system", "idle"])(*cpus)
        pids_mock.return_value = list(range(1, 39))
        process_mock.side_effect = self._generate_process
        fp = tempfile.NamedTemporaryFile()
        try:
            parse_mock.return_value = namedtuple('Parse', ["i", "f", "n"])(1, fp.name, 2)
            snapshot.main()

            count = 0
            with open(fp.name) as f:
                for line in f:
                    self.assertEqual(json.loads(line), expected)
                    count += 1

            self.assertEqual(count, 2)
            print_mock.assert_called_with(expected, end="\r")
            sleep_mock.assert_called_with(1)

            parse_mock.return_value = namedtuple('Parse', ["i", "f", "n"])(1, fp.name, 1)
            snapshot.main()

            count = 0
            with open(fp.name) as f:
                for line in f:
                    self.assertEqual(json.loads(line), expected)
                    count += 1

            self.assertEqual(count, 1)
        finally:
            fp.close()
