from pathlib import Path
from monitor.notifier import send_notification

LOG_FILE = Path("logs/app.log")


def analyze_logs(last_position):

    if not LOG_FILE.exists():
        return last_position

    with LOG_FILE.open("r", encoding="utf-8") as file:
        file.seek(last_position)
        lines = file.readlines()
        new_position = file.tell()

    for line in lines:
        if "ERROR" in line:
            send_notification(f"ALERT: {line.strip()}")
    return new_position


if __name__ == "__main__":
    position = 0
    position = analyze_logs(position)
