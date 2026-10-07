import os
import unittest
from unittest.mock import patch

from monitor.notifier import send_notification


class TestNotifier(unittest.TestCase):
    def test_without_webhook_does_not_send_request(self):
        with patch.dict(os.environ, {}, clear=True):
            with patch("monitor.notifier.urlopen") as mock_urlopen:
                send_notification("Test alert")

        mock_urlopen.assert_not_called()

    def test_with_webhook_sends_request(self):
        test_env = {
            "DISCORD_WEBHOOK_URL": "https://example.com/webhook"
        }

        with patch.dict(os.environ, test_env):
            with patch("monitor.notifier.urlopen") as mock_urlopen:
                send_notification("Test alert")

        mock_urlopen.assert_called_once()