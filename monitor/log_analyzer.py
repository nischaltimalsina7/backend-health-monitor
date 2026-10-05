from pathlib import Path


LOG_FILE = Path("logs/app.log")


def analyze_logs(last_position):
    with LOG_FILE.open("r", encoding="utf-8") as file:
        file.seek(last_position)
        lines = file.readlines()
        new_position = file.tell()

    for line in lines:
        if "ERROR" in line:
            print(f"ALERT: {line.strip()}")
    return new_position


if __name__ == "__main__":
    position = 0
    position = analyze_logs(position)
