import json
import sys
from collections import Counter
from pathlib import Path

log_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("evidence/authentication.log")
report_file = Path("reports/alerts.json")

normal_ip = "10.10.20.15"
failed_threshold = 3

successful_logins = []
failed_logins = []
unusual_successful_logins = []
ip_activity = Counter()
failed_by_user = Counter()
alerts = []

with log_file.open("r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if "SUCCESS" in line:
            successful_logins.append(line)

            if "source_ip=" in line:
                ip = line.split("source_ip=")[1].split()[0]
                ip_activity[ip] += 1

                if ip != normal_ip:
                    unusual_successful_logins.append(line)
                    alerts.append({
                        "type": "unusual_successful_login",
                        "severity": "medium",
                        "event": line
                    })

        elif "FAILED" in line:
            failed_logins.append(line)

            if "user=" in line:
                user = line.split("user=")[1].split()[0]
                failed_by_user[user] += 1

for user, count in failed_by_user.items():
    if count >= failed_threshold:
        alerts.append({
            "type": "repeated_failed_logins",
            "severity": "medium",
            "user": user,
            "failed_attempts": count
        })

report_file.parent.mkdir(parents=True, exist_ok=True)

report = {
    "summary": {
        "successful_logins": len(successful_logins),
        "failed_logins": len(failed_logins),
        "alerts_generated": len(alerts)
    },
    "alerts": alerts,
    "successful_logins_by_ip": dict(ip_activity)
}

with report_file.open("w", encoding="utf-8") as file:
    json.dump(report, file, indent=2)

print("=== Authentication Log Analysis ===")
print(f"Successful logins: {len(successful_logins)}")
print(f"Failed logins: {len(failed_logins)}")

print("\n=== Unusual Successful Login Alerts ===")
for event in unusual_successful_logins:
    print(f"ALERT: {event}")

print("\n=== Repeated Failed Login Alerts ===")
alerts_found = False

for user, count in failed_by_user.items():
    if count >= failed_threshold:
        print(f"ALERT: {user} has {count} failed login attempts")
        alerts_found = True

if not alerts_found:
    print("No repeated failed login threshold reached.")

print("\n=== Successful Login Counts by IP ===")
for ip, count in ip_activity.items():
    print(f"{ip}: {count} successful login(s)")

print(f"\nJSON alert report saved to: {report_file}")
