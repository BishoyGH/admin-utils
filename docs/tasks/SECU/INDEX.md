# SECU — Security Center: tasks

Spec: [`14-security-center.md`](../../specs/14-security-center.md) · 30 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [SECU-001](SECU-001.md) | P0 | 1 | todo | Security dashboard: score, open findings, trend |
| [SECU-002](SECU-002.md) | P0 | 1 | todo | Password policy review (length, complexity, expiry settings) with recommendations |
| [SECU-003](SECU-003.md) | P0 | 1 | todo | 2FA enforcement coverage and exemptions report |
| [SECU-004](SECU-004.md) | P0 | 1 | todo | Login security settings review (lockout, session timeout, IP restrictions) |
| [SECU-005](SECU-005.md) | P0 | 1 | todo | Admin/System Manager account inventory and activity summary |
| [SECU-006](SECU-006.md) | P1 | 4 | todo | Inactive user detection and auto-disable policy |
| [SECU-007](SECU-007.md) | P1 | 4 | todo | Shared account detector (multiple IPs/devices rapidly) |
| [SECU-008](SECU-008.md) | P1 | 4 | todo | API key and token inventory with last-used and owner |
| [SECU-009](SECU-009.md) | P1 | 4 | todo | Open guest-access check (doctypes/pages/methods exposed to Guest) |
| [SECU-010](SECU-010.md) | P1 | 4 | todo | Whitelisted method exposure scanner (allow_guest, unprotected methods) |
| [SECU-011](SECU-011.md) | P1 | 4 | todo | File exposure scan (public files that look private) |
| [SECU-012](SECU-012.md) | P1 | 4 | todo | Secrets-in-data scanner (tokens/passwords pasted into text fields, opt-in) |
| [SECU-013](SECU-013.md) | P1 | 4 | todo | Security headers and cookie flags check |
| [SECU-014](SECU-014.md) | P1 | 4 | todo | HTTPS/HSTS and certificate checks |
| [SECU-015](SECU-015.md) | P1 | 4 | todo | Dangerous settings check (developer mode, allow_tests, server scripts enabled) |
| [SECU-016](SECU-016.md) | P1 | 4 | todo | Server Script and Client Script risk review |
| [SECU-017](SECU-017.md) | P1 | 4 | todo | Webhook endpoint review (HTTP vs HTTPS, secrets configured) |
| [SECU-018](SECU-018.md) | P1 | 4 | todo | Audit trail anomaly detection (bulk deletes, off-hours admin actions) |
| [SECU-019](SECU-019.md) | P1 | 4 | todo | Failed login analytics with IP reputation hooks (local lists) |
| [SECU-020](SECU-020.md) | P1 | 4 | todo | Security findings workflow (open, accepted risk, fixed) with owner and due date |
| [SECU-021](SECU-021.md) | P2 | 11 | todo | Periodic security scan scheduler and report email |
| [SECU-022](SECU-022.md) | P2 | 11 | todo | Hardening checklist mapped to OWASP ASVS and CIS-style controls |
| [SECU-023](SECU-023.md) | P2 | 11 | todo | Security baseline snapshot and drift alerts |
| [SECU-024](SECU-024.md) | P2 | 11 | todo | Incident response playbook runner (lock user, rotate keys, revoke sessions) |
| [SECU-025](SECU-025.md) | P2 | 11 | todo | Emergency "lockdown mode" (read-only site, block non-admin logins) |
| [SECU-026](SECU-026.md) | P2 | 11 | todo | IP allowlist manager for admin routes |
| [SECU-027](SECU-027.md) | P2 | 11 | todo | Honeypot field/endpoint alerts (opt-in) |
| [SECU-028](SECU-028.md) | P2 | 11 | todo | Data classification tags per doctype/field (public, internal, confidential) |
| [SECU-029](SECU-029.md) | P2 | 11 | todo | Export of security evidence pack for audits |
| [SECU-030](SECU-030.md) | P2 | 11 | todo | Third-party app risk inventory (installed apps, versions, known advisories feed) |
