from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from unittest.mock import patch

from monitor.state import load_log_position, save_log_position


class TestState(unittest.TestCase):
    def test_load_position_when_file_missing(self):
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "log_position.txt"

            with patch("monitor.state.POSITION_FILE", test_file):
                position = load_log_position()

            self.assertEqual(position, 0)

    def test_save_and_load_position(self):
        with TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "log_position.txt"

            with patch("monitor.state.POSITION_FILE", test_file):
                save_log_position(390)
                position = load_log_position()

            self.assertEqual(position, 390)