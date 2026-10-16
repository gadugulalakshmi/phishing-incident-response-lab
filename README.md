# Phishing Incident Response Lab

## Project Overview

This project simulates a phishing attack that may lead to
user credential compromise. It demonstrates a structured
incident response workflow and basic authentication log analysis.

## Objectives

- Understand phishing incident response.
- Identify suspicious authentication activity.
- Document Indicators of Compromise (IoCs).
- Build an incident timeline.
- Automate basic log analysis using Python.
- Recommend containment, eradication, and recovery actions.

## Tools Used

- Kali Linux
- Python 3
- Linux Terminal
- Markdown
- Sample authentication logs

## Project Structure

- docs/: Incident scenario, playbook, timeline, and report
- evidence/: Simulated authentication logs and IoCs
- scripts/: Python authentication log analyzer

## Detection Logic

The Python script identifies successful logins from IP addresses
that differ from the configured normal IP baseline. It also
counts successful and failed authentication events.

## Key Findings

In the sample dataset, two successful logins originated from
an IP address different from the configured baseline.

These events were flagged for investigation. An unusual IP
address alone does not prove malicious activity.

## Incident Response Lifecycle

1. Preparation
2. Detection and Analysis
3. Containment
4. Eradication
5. Recovery
6. Post-Incident Activity

## Limitations

This is a simulated training project using sample data.
It has not been tested against a production environment.

## Future Improvements

- Parse logs using structured fields.
- Generate a machine-readable alert report.
- Add a dedicated automated test suite for the Python script.
- Improve detection logic with configurable IP baselines and thresholds.
