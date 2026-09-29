def update_incident(result, failures, incident_open):
    if result["status"] == "DOWN":
        failures += 1

        if failures >= 3 and not incident_open:
            incident_open = True
            return failures, incident_open, "ALERT: Backend is down"

        return failures, incident_open, None

    failures = 0

    if incident_open:
        incident_open = False
        return failures, incident_open, "RECOVERED: Backend is up again"

    return failures, incident_open, None