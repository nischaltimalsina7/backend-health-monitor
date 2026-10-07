# Backend Health & Log Monitor

A Python-based backend monitoring system that automatically checks service health, measures response time, detects failures and application errors, and sends alerts when problems occur.

## Features

- Automatic backend health monitoring
- HTTP status and response-time tracking
- High-latency detection
- Incident detection after consecutive failures
- Recovery detection
- Application log analysis
- ERROR log detection
- Persistent log monitoring position across restarts
- Monitoring history stored in JSONL format
- Configurable monitoring URL, check interval, and latency threshold
- Terminal alert notifications
- Optional Discord webhook notifications
- Graceful handling of missing application log files
- Automated tests for monitoring components

## How It Works

The monitor periodically sends an HTTP request to a configured health endpoint.

Each check records information such as:

- Timestamp
- Service status
- HTTP status code
- Response latency
- High-latency status
- Connection errors

The results are stored in:

```text
data/checks.jsonl
```

If the backend fails three consecutive health checks, the system opens an incident and sends an alert.

When the backend becomes available again, the system sends a recovery notification.

The monitor also analyzes application logs for new `ERROR` entries. It saves its last log position so previously processed errors are not reported again after the monitor restarts.

## Project Structure

```text
backend-health-monitor/
├── monitor/
│   ├── checker.py
│   ├── config.py
│   ├── incidents.py
│   ├── log_analyzer.py
│   ├── notifier.py
│   ├── scheduler.py
│   ├── state.py
│   └── storage.py
│
├── tests/
│   ├── test_config.py
│   ├── test_incidents.py
│   ├── test_log_analyzer.py
│   ├── test_notifier.py
│   └── test_state.py
│
├── data/
├── logs/
├── test_service.py
├── requirements.txt
└── README.md
```

## Run Locally

Create a Python virtual environment:

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Start the Test Backend

Start the included FastAPI test service:

```powershell
python -m uvicorn test_service:app --port 8000
```

The health endpoint is:

```text
http://127.0.0.1:8000/health
```

A successful request returns:

```json
{"status": "ok"}
```

Keep this terminal running.

## Start the Monitor

Open a second PowerShell terminal, activate the virtual environment, and run:

```powershell
python -m monitor.scheduler
```

By default, the monitor checks:

```text
http://127.0.0.1:8000/health
```

every 5 seconds.

Press `Ctrl+C` to stop the monitor.

## Configuration

The monitor can be configured using environment variables.

### Monitoring URL

Default:

```text
http://127.0.0.1:8000/health
```

Example:

```powershell
$env:MONITOR_URL="https://example.com/health"
```

### Check Interval

The default check interval is 5 seconds.

Example:

```powershell
$env:CHECK_INTERVAL_SECONDS="10"
```

### Latency Threshold

The default high-latency threshold is 500 milliseconds.

Example:

```powershell
$env:LATENCY_THRESHOLD_MS="1000"
```

## Incident Detection

The monitor tracks consecutive failed health checks.

After three consecutive failures, it sends:

```text
ALERT: Backend is down
```

Additional failed checks do not repeatedly create the same incident.

When the backend becomes available again, it sends:

```text
RECOVERED: Backend is up again
```

## Application Log Monitoring

The monitor analyzes:

```text
logs/app.log
```

New lines containing `ERROR` generate notifications.

The last processed log position is stored in:

```text
data/log_position.txt
```

This prevents previously processed errors from being reported again after restarting the monitor.

If the application log does not exist, the monitor continues running instead of crashing.

## Discord Notifications

Terminal notifications work by default.

Discord notifications are optional and use a webhook URL stored in an environment variable.

Set the webhook in PowerShell:

```powershell
$env:DISCORD_WEBHOOK_URL="<your-discord-webhook-url>"
```

Then start the monitor normally:

```powershell
python -m monitor.scheduler
```

Alerts, recovery messages, and detected application errors can then be sent to Discord.

### Security

Never place the real Discord webhook URL directly in the source code.

Do not commit webhook URLs, passwords, API keys, or other credentials to Git.

## Monitoring History

Health-check results are saved to:

```text
data/checks.jsonl
```

Each line contains one JSON monitoring result, making the history easy to process later.

Example:

```json
{
  "status": "UP",
  "http_status": 200,
  "latency_ms": 42.5,
  "high_latency": false,
  "error": null
}
```

## Run Automated Tests

Run the complete test suite with:

```powershell
python -m unittest discover -s tests
```

The project currently includes automated tests for:

- Incident detection
- Persistent log position state
- Application log analysis
- Missing log-file handling
- Configuration
- Notification behavior

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Python `unittest`
- HTTP/REST
- JSON / JSONL
- Discord Webhooks
- Git
- GitHub

## Current Status

The core monitoring system is implemented and tested.

It supports health monitoring, latency detection, incident and recovery handling, application log analysis, persistent monitoring state, configurable settings, terminal notifications, and optional Discord alerts.