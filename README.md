# Backend Health & Log Monitor

A backend monitering system for detecting service failures, high latency,
and application errors.

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

## Run locally

Use Python in the project folder. On Windows PowerShell, create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Start the test backend in one terminal:

```powershell
python -m uvicorn test_service:app --reload
```

Open http://127.0.0.1:8000/health to check that it returns `{"status":"ok"}`.

In a second terminal, start the monitor:

```powershell
python -m monitor.scheduler
```

The monitor checks every five seconds and saves results to `data/checks.jsonl`. It announces an alert after three consecutive failed checks and announces recovery when a check succeeds again. Press Ctrl+C in the monitor terminal to stop it.

Run the incident test with:

```powershell
python -m unittest discover -s tests -v
```
## Running the Test Service

Start the FastAPI test service:

```powershell
python -m uvicorn test_service:app --port 8000