from datetime import datetime, timezone
from time import perf_counter
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from monitor.config import LATENCY_THRESHOLD_MS




def check_health(url):
    checked_at = datetime.now(timezone.utc).isoformat()
    start = perf_counter()

    try:
        with urlopen(url, timeout=5) as response:
            elapsed_ms = (perf_counter() - start) * 1000
            high_latency = elapsed_ms >= LATENCY_THRESHOLD_MS

            return {
                "checked_at": checked_at,
                "status": "UP",
                "http_status": response.status,
                "latency_ms": round(elapsed_ms, 1),
                "high_latency": high_latency,
                "error": None,
            }

    except HTTPError as error:
        elapsed_ms = (perf_counter() - start) * 1000

        return {
            "checked_at": checked_at,
            "status": "DOWN",
            "http_status": error.code,
            "latency_ms": round(elapsed_ms, 1),
            "error": str(error),
        }

    except URLError as error:
        elapsed_ms = (perf_counter() - start) * 1000

        return {
            "checked_at": checked_at,
            "status": "DOWN",
            "http_status": None,
            "latency_ms": round(elapsed_ms, 1),
            "error": str(error.reason),
        }


if __name__ == "__main__":
    result = check_health("http://127.0.0.1:8000/health")
    print(result)