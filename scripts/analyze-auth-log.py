from collections import Counter

log_file = "../evidence/authentication.log"
normal_ip = "10.10.20.15"

successful_logins = []
failed_logins = []
unusual_successful_logins = []
ip_activity = Counter()

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

print("=== Authentication Log Analysis ===")
print(f"Successful logins: {len(successful_logins)}")
print(f"Failed logins: {len(failed_logins)}")

print("\n=== Successful Logins from Unusual IPs ===")

if unusual_successful_logins:
    for event in unusual_successful_logins:
        print(f"ALERT: {event}")
else:
    print("No unusual successful logins detected.")

print("\n=== Successful Login Counts by IP ===")

for ip, count in ip_activity.items():
    print(f"{ip}: {count} successful login(s)")
