from collections import Counter, defaultdict

log_file = "evidence/authentication.log"
normal_ip = "10.10.20.15"
failed_threshold = 3

successful_logins = []
failed_logins = []
unusual_successful_logins = []
ip_activity = Counter()
failed_by_user = Counter()

with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if "SUCCESS" in line:
            successful_logins.append(line)

            if "source_ip=" in line:
                ip = line.split("source_ip=")[1].split()[0]
                ip_activity[ip] += 1

                if ip != normal_ip:
                    unusual_successful_logins.append(line)

        elif "FAILED" in line:
            failed_logins.append(line)

            if "user=" in line:
                user = line.split("user=")[1].split()[0]
                failed_by_user[user] += 1

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
