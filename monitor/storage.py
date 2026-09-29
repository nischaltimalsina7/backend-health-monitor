import json
from pathlib import Path


RESULTS_FILE = Path("data/checks.jsonl")


def save_result(result):
    RESULTS_FILE.parent.mkdir(exist_ok=True)

    with RESULTS_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(result) + "\n")