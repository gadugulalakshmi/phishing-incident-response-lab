# Phishing Incident Response Lab

## Project Overview

This project simulates a phishing attack that may lead to user credential compromise. It demonstrates a structured incident response workflow and automated authentication log analysis using Python.

## Objectives

- Understand phishing incident response.
- Identify suspicious authentication activity.
- Document Indicators of Compromise (IoCs).
- Build an incident timeline.
- Automate authentication log analysis using Python.
- Generate a machine-readable JSON alert report.
- Recommend containment, eradication, and recovery actions.
- Validate core functionality using automated tests.

## Tools Used

- Kali Linux
- Python 3
- Git and GitHub
- Linux Terminal
- JSON
- Markdown
- Python `unittest`

## Project Structure

```text
IR-Playbook/
├── docs/
│   ├── incident-report.md
│   ├── incident-timeline.md
│   ├── incident-scenario.md
│   └── phishing-ir-playbook.md
├── evidence/
│   ├── authentication.log
│   ├── test-authentication.log
│   └── indicators-of-compromise.md
├── reports/
│   └── alerts.json
├── scripts/
│   └── analyze-auth-log.py
├── tests/
│   └── test_analyzer.py
└── README.md
```

## Detection Logic

The Python analyzer:

- Counts successful and failed authentication events.
- Flags successful logins from IP addresses outside the configured baseline.
- Counts failed login attempts by user.
- Generates alerts when the configured failed-login threshold is reached.
- Summarizes successful logins by source IP address.
- Saves alert details and summary statistics to a JSON report.

## Sample Results

The sample authentication log contains:

- 3 successful login events.
- 1 failed login event.
- 2 unusual successful login alerts.
- A generated JSON report at `reports/alerts.json`.

The suspicious successful logins originated from `185.220.101.45`, which differs from the configured baseline IP `10.10.20.15`.

These events warrant investigation. An unfamiliar IP address alone does not prove malicious activity.

## Running the Analyzer

From the project root directory, run:

```bash
python3 scripts/analyze-auth-log.py
```

The script displays authentication statistics and alerts in the terminal and generates `reports/alerts.json`.

## Running Automated Tests

Run the test suite with:

```bash
python3 -m unittest discover -s tests -v
```

The tests verify that the analyzer executes successfully and that the JSON report is generated with the expected sample counts and alerts.

## Incident Response Lifecycle

1. Preparation
2. Detection and Analysis
3. Containment
4. Eradication
5. Recovery
6. Post-Incident Activity

## Limitations

This is a simulated training project using sample data. The detection logic uses a simple configured IP baseline and failed-login threshold. It has not been validated in a production environment.

## Future Improvements

- Parse logs using structured fields.
- Make IP baselines and thresholds configurable.
- Expand automated tests to cover more detection scenarios.
- Improve alert severity and reporting.
- Integrate additional log sources.

