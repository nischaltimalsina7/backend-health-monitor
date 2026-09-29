import unittest

from monitor.incidents import update_incident


class IncidentTests(unittest.TestCase):
    def test_alert_once_then_recovery(self):
        statuses = ["DOWN", "DOWN", "DOWN", "DOWN", "UP"]
        messages = []
        failures = 0
        incident_open = False

        for status in statuses:
            result = {"status": status}
            failures, incident_open, message = update_incident(
                result, failures, incident_open
            )
            if message is not None:
                messages.append(message)

        self.assertEqual(
            messages,
            ["ALERT: Backend is down", "RECOVERED: Backend is up again"],
        )
        self.assertEqual(failures, 0)
        self.assertFalse(incident_open)


if __name__ == "__main__":
    unittest.main()