import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from monitor.log_analyzer import analyze_logs

class TestLogAnalyzer(unittest.TestCase):
    def test_info_log_does_not_notify(self):
        with TemporaryDirectory() as temp_dir:
            test_log = Path(temp_dir) / "app.log"
            test_log.write_text(
                "2026-10-05 19:00:00 INFO Server started\n",
                encoding="utf-8",
            )

            with patch("monitor.log_analyzer.LOG_FILE", test_log):
                with patch("monitor.log_analyzer.send_notification") as mock_notify:
                    analyze_logs(0)

            mock_notify.assert_not_called()

    def test_error_log_sends_notification(self):
        with TemporaryDirectory() as temp_dir:
            test_log = Path(temp_dir) / "app.log"
            test_log.write_text(
                "2026-10-05 19:00:00 ERROR Database connection failed\n",
                encoding="utf-8",
            )

            with patch("monitor.log_analyzer.LOG_FILE", test_log):
                with patch("monitor.log_analyzer.send_notification") as mock_notify:
                    analyze_logs(0)

            mock_notify.assert_called_once()

    def test_missing_log_file_does_not_crash(self):
        with TemporaryDirectory() as temp_dir:
            missing_log = Path(temp_dir) / "missing.log"

            with patch("monitor.log_analyzer.LOG_FILE", missing_log):
                position = analyze_logs(100)

            self.assertEqual(position, 100)