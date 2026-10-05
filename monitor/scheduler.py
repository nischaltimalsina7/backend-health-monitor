from time import sleep

from monitor.checker import check_health
from monitor.incidents import update_incident
from monitor.storage import save_result
from monitor.log_analyzer import analyze_logs


def main():
    url = "http://127.0.0.1:8000/health"
    failures = 0
    incident_open = False
    log_position = 0

    try:
        while True:
            result = check_health(url)
            save_result(result)
            print(result)
            log_position = analyze_logs(log_position)

            if result.get("high_latency"):
                print("WARNING: High latency detected") 

            failures, incident_open, message = update_incident(
                result, failures, incident_open
            )

            if message is not None:
                print(message)

            sleep(5)

    except KeyboardInterrupt:
        print("\nMonitor stopped.")


if __name__ == "__main__":
    main()