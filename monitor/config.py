import os


MONITOR_URL = os.getenv(
    "MONITOR_URL",
    "http://127.0.0.1:8000/health",
)

LATENCY_THRESHOLD_MS = int(
    os.getenv("LATENCY_THRESHOLD_MS", "500")
)

CHECK_INTERVAL_SECONDS = int(
    os.getenv("CHECK_INTERVAL_SECONDS", "5")
)