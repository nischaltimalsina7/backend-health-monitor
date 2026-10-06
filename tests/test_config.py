import importlib
import os
import unittest
from unittest.mock import patch

import monitor.config as config

from monitor.config import (
    MONITOR_URL,
    LATENCY_THRESHOLD_MS,
    CHECK_INTERVAL_SECONDS,
)


class TestConfig(unittest.TestCase):
    def test_default_values(self):
        self.assertEqual(MONITOR_URL, "http://127.0.0.1:8000/health")
        self.assertEqual(LATENCY_THRESHOLD_MS, 500)
        self.assertEqual(CHECK_INTERVAL_SECONDS, 5)

    def test_environment_values(self):
        test_env = {
            "MONITOR_URL": "https://example.com/health",
            "LATENCY_THRESHOLD_MS": "100",
            "CHECK_INTERVAL_SECONDS": "2",
        }

        with patch.dict(os.environ, test_env):
            importlib.reload(config)

            self.assertEqual(
                config.MONITOR_URL,
                "https://example.com/health",
            )
            self.assertEqual(config.LATENCY_THRESHOLD_MS, 100)
            self.assertEqual(config.CHECK_INTERVAL_SECONDS, 2)