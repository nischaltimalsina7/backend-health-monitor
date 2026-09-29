from time import sleep

from monitor.checker import check_health
from monitor.storage import save_result


def main():
    url = "http://127.0.0.1:8000/health"

    try:
        while True:
            result = check_health(url)
            save_result(result)
            print(result)
            sleep(5)
    except KeyboardInterrupt:
        print("\nMonitor stopped.")


if __name__ == "__main__":
    main()