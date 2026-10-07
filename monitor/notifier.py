import os
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

def send_notification(message):
    print(f"NOTIFICATION: {message}")

    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        return

    payload = {
    "content": message
}

    data = json.dumps(payload).encode("utf-8")

    request = Request(
    webhook_url,
    data=data,
    headers={
    "Content-Type": "application/json",
    "User-Agent": "BackendHealthMonitor/1.0",
    },
    method="POST",
)
    try:
        with urlopen(request, timeout=5):
            pass

    except (HTTPError, URLError) as error:
        print(f"NOTIFICATION ERROR: {error}")

