from time import perf_counter
from urllib.error import URLError
from urllib.request import urlopen


def check_health(url):
    start = perf_counter()

    try:
        with urlopen(url, timeout=5) as response:
            elapsed_ms = (perf_counter() - start) * 1000

            return {
                "status": "UP",
                "http_status": response.status,
                "latency_ms": round(elapsed_ms, 1),
            }

    except URLError:
        return {
            "status": "DOWN",
            "http_status": None,
            "latency_ms": None,
        }


if __name__ == "__main__":
    result = check_health("http://127.0.0.1:8000/health")
    print(result)