# Indicators of Compromise

## Incident
Phishing Attack Leading to Account Compromise

## Identified Indicators

| Indicator | Value | Significance |
|---|---|---|
| Affected User | alice | Potentially compromised account |
| Phishing Event | phishing_link_clicked | User interacted with phishing content |
| Credential Event | credentials_submitted | Credentials may have been exposed |
| Suspicious IP | 185.220.101.45 | Unusual external source |
| Suspicious Location | Unknown | Location differs from normal activity |
| Failed Login | 10:13:17 | Additional suspicious authentication activity |
| Successful Login | 10:14:02 | Successful access from suspicious source |

## Assessment

The combination of a phishing event, credential submission, and
successful authentication from an unusual source indicates a
potential compromise of the affected account.

## Recommended Response

- Disable or restrict the affected account.
- Revoke active sessions and authentication tokens.
- Reset the account password.
- Verify and reset MFA if required.
- Continue monitoring authentication activity.
