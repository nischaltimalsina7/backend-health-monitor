from pathlib import Path


POSITION_FILE = Path("data/log_position.txt")


def load_log_position():
    if not POSITION_FILE.exists():
        return 0

    position = POSITION_FILE.read_text(encoding="utf-8")
    return int(position)


def save_log_position(position):
    POSITION_FILE.parent.mkdir(exist_ok=True)
    POSITION_FILE.write_text(str(position), encoding="utf-8")