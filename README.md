# Backend Health & Log Monitor

A backend monitoring system for detecting service failures, high latency, and application errors.

## Project Status

Currently under development.

## Planned Features

- Service health monitoring
- Response time tracking
- Failure detection
- Incident management
- Log analysis
- Alert notifications
- Monitoring history

## Run Locally

Use Python in the project folder. On Windows PowerShell, create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Start the test backend in one terminal:

```powershell
python -m uvicorn test_service:app --port 8000
```

Open `http://127.0.0.1:8000/health` in your browser.

A successful response should return:

```json
{"status": "ok"}
```

In a second terminal, start the monitor:

```powershell
python -m monitor.scheduler
```

The monitor checks the backend every five seconds and saves the results to `data/checks.jsonl`.

After three consecutive failed checks, it reports:

```text
ALERT: Backend is down
```

When the backend becomes available again, it reports:

```text
RECOVERED: Backend is up again
```

Press `Ctrl+C` in the monitor terminal to stop the monitor.

## Run Tests

Run the incident tests with:

```powershell
python -m unittest discover -s tests -v
```