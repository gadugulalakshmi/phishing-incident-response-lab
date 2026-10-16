
# Phishing Incident Response Playbook

## 1. Preparation

### Objective
Ensure the organization is prepared to detect, investigate, contain,
and recover from phishing-related security incidents.

### Preparation Checklist
- Define incident response roles and responsibilities.
- Ensure authentication and security logs are available.
- Maintain an inventory of critical accounts and systems.
- Enable multi-factor authentication (MFA) where possible.
- Maintain secure backups of important data.
- Provide phishing awareness training to employees.
- Maintain documented incident response procedures.
- Establish communication and escalation procedures.

### Key Roles
- Incident Response Lead
- SOC / Security Analyst
- IT Administrator
- System Owner
- Management / Incident Coordinator

### Expected Outcome
The organization has the people, procedures, access, and evidence
sources required to respond quickly to a phishing incident.

## 2. Detection and Analysis

### Objective
Identify and analyze indicators of a phishing attack and determine
whether an account has been compromised.

### Detection Sources
- User-reported phishing email
- Email security alerts
- Authentication and login logs
- SIEM alerts
- Endpoint security alerts
- Suspicious URL or domain reports

### Investigation Steps

1. Collect the original phishing email and preserve it as evidence.
2. Identify the sender address and inspect email headers.
3. Extract and examine URLs contained in the email.
4. Check whether the user clicked the suspicious URL.
5. Review authentication logs for unusual login activity.
6. Identify suspicious source IP addresses and login locations.
7. Review account activity after the suspected compromise.
8. Build a timeline of the incident.
9. Determine the scope and severity of the incident.

### Indicators of Compromise
- Suspicious sender address
- Malicious or suspicious URL
- Unknown source IP address
- Unusual geographic login location
- Multiple failed login attempts
- Successful login after suspicious activity
- Unexpected account activity

### Analysis Decision

If the evidence confirms that the phishing email resulted in
credential compromise, escalate the incident to the containment phase.

If the evidence does not support compromise, document the findings
and close the investigation.

### Expected Outcome
The security team confirms whether the phishing incident is genuine,
identifies affected accounts and systems, and documents the available
evidence for containment and response.

## 3. Containment

### Objective
Prevent the attacker from gaining further access and limit the impact
of the compromised account.

### Containment Actions

1. Temporarily disable the compromised user account.
2. Revoke active sessions and authentication tokens.
3. Reset the user's password.
4. Reset or reconfigure MFA if compromise is suspected.
5. Block the malicious URL or domain.
6. Isolate any affected endpoint from the network if required.
7. Preserve relevant logs and evidence for further investigation.
8. Notify the appropriate security and IT teams.

### Containment Decision

If the account is confirmed to be compromised, immediately restrict
access and continue monitoring for additional suspicious activity.

If no compromise is confirmed, continue monitoring the account and
document the investigation findings.

### Expected Outcome
The compromised account and affected systems are contained, further
unauthorized access is prevented, and relevant evidence is preserved
for remediation and recovery.

## 4. Eradication

### Objective
Remove the root cause of the phishing incident and eliminate any
remaining threats from affected accounts and systems.

### Eradication Actions

1. Remove or quarantine the phishing email from affected mailboxes.
2. Block the malicious URL and domain across security controls.
3. Invalidate compromised credentials and authentication tokens.
4. Remove unauthorized account changes made by the attacker.
5. Search for additional affected accounts or systems.
6. Remove any malware or malicious files found on affected endpoints.
7. Review security configurations for signs of attacker changes.
8. Confirm that no additional persistence mechanisms remain.

### Verification

The security team must verify that the phishing indicators are no
longer active and that the attacker no longer has unauthorized access.

### Expected Outcome
The phishing threat and attacker access have been removed, affected
accounts and systems are clean, and the environment is ready for
recovery.

## 5. Recovery

### Objective
Restore affected accounts and systems to normal operation while
continuing to monitor for signs of compromise.

### Recovery Actions

1. Re-enable the user account after security checks are completed.
2. Set a new secure password for the affected account.
3. Verify that MFA is enabled and functioning correctly.
4. Revoke any remaining suspicious sessions or tokens.
5. Confirm that the affected endpoint is clean before reconnecting it.
6. Monitor authentication and account activity for unusual behavior.
7. Confirm that normal business operations have been restored.
8. Continue enhanced monitoring for a defined period.

### Recovery Verification

The security team must verify that the account and affected systems
are operating normally and that no further suspicious activity is
detected.

### Expected Outcome
Affected accounts and systems are safely restored to normal operation,
with continued monitoring to detect any recurring or related activity.

## 6. Post-Incident Activity

### Objective
Review the incident, document lessons learned, and improve security
controls and incident response procedures.

### Post-Incident Actions

1. Document the complete incident timeline.
2. Record the root cause and contributing factors.
3. Document the actions taken during detection, containment,
   eradication, and recovery.
4. Identify what worked well and what could be improved.
5. Review whether security controls detected the incident effectively.
6. Improve phishing awareness training if required.
7. Update security controls and monitoring based on findings.
8. Update the incident response playbook with lessons learned.
9. Prepare a final incident report.
10. Share relevant findings with appropriate stakeholders.

### Lessons Learned

The organization should identify improvements that can reduce the
likelihood and impact of similar phishing incidents in the future.

### Expected Outcome
The incident is fully documented, lessons are captured, security
controls are improved, and the organization is better prepared for
future phishing incidents.
