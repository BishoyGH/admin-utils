# F2B — Fail2ban Integration: tasks

Spec: [`11-fail2ban.md`](../../specs/11-fail2ban.md) · 40 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [F2B-001](F2B-001.md) | P0 | 4 | todo | Detect fail2ban installation, version and service state (read-only) |
| [F2B-002](F2B-002.md) | P0 | 4 | todo | Privileged helper design: minimal sudoers rule limited to specific `fail2ban-client` subcommands |
| [F2B-003](F2B-003.md) | P0 | 4 | todo | List jails and their status (currently failed/banned, totals) |
| [F2B-004](F2B-004.md) | P0 | 4 | todo | List banned IPs per jail with ban time |
| [F2B-005](F2B-005.md) | P0 | 4 | todo | Unban IP (validated IPv4/IPv6 only) with audit entry |
| [F2B-006](F2B-006.md) | P0 | 4 | todo | Manual ban IP with duration and reason |
| [F2B-007](F2B-007.md) | P0 | 4 | todo | Role gate `Admin Utils Security Admin` |
| [F2B-008](F2B-008.md) | P0 | 4 | todo | Safe-by-default: feature disabled until helper configured and verified |
| [F2B-009](F2B-009.md) | P1 | 4 | todo | Self-lockout protection (warn/block banning your own IP and allowlisted ranges) |
| [F2B-010](F2B-010.md) | P1 | 4 | todo | Whitelist (ignoreip) viewer and managed editor with backups |
| [F2B-011](F2B-011.md) | P1 | 4 | todo | Jail enable/disable for allowlisted jails |
| [F2B-012](F2B-012.md) | P1 | 4 | todo | Filter/jail config templates for Frappe login failures (nginx/access log pattern) |
| [F2B-013](F2B-013.md) | P1 | 4 | todo | Filter regex tester against sample log lines |
| [F2B-014](F2B-014.md) | P1 | 4 | todo | Ban log timeline and search (IP, jail, date) |
| [F2B-015](F2B-015.md) | P1 | 4 | todo | GeoIP info for banned IPs (local DB only, no external calls by default) |
| [F2B-016](F2B-016.md) | P1 | 4 | todo | Statistics (bans per day, top offenders, top jails) |
| [F2B-017](F2B-017.md) | P1 | 4 | todo | Link failed Frappe logins to bans (cross-reference Activity Log) |
| [F2B-018](F2B-018.md) | P1 | 4 | todo | Alerts when ban spikes occur |
| [F2B-019](F2B-019.md) | P1 | 4 | todo | Bulk unban and bulk ban from CSV with preview |
| [F2B-020](F2B-020.md) | P1 | 4 | todo | Reload fail2ban config safely with config test first |
| [F2B-021](F2B-021.md) | P1 | 4 | todo | Config backup/restore before any change |
| [F2B-022](F2B-022.md) | P2 | 11 | todo | Permanent ban list management (recidive jail view) |
| [F2B-023](F2B-023.md) | P2 | 11 | todo | Ban duration policy presets (progressive durations) |
| [F2B-024](F2B-024.md) | P2 | 11 | todo | Integration with Frappe rate-limit/login-attempt settings for consistent thresholds |
| [F2B-025](F2B-025.md) | P2 | 11 | todo | Notification on ban/unban events |
| [F2B-026](F2B-026.md) | P2 | 11 | todo | Export banned IP list |
| [F2B-027](F2B-027.md) | P2 | 11 | todo | Setup wizard generating install commands for the operator to run (not executed by app) |
| [F2B-028](F2B-028.md) | P2 | 11 | todo | Dry-run simulation of a filter on recent logs |
| [F2B-029](F2B-029.md) | P2 | 11 | todo | Optional nftables/iptables read-only status view |
| [F2B-030](F2B-030.md) | P2 | 11 | todo | Compatibility notes per distro (Ubuntu/Debian/Alma/Rocky) |

## Additional capabilities

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [F2B-031](F2B-031.md) | P1 | 9 | todo | Per-jail configuration viewer (maxretry, findtime, bantime) with human explanations |
| [F2B-032](F2B-032.md) | P1 | 9 | todo | Safe editing of selected jail parameters with validation and backup |
| [F2B-033](F2B-033.md) | P1 | 9 | todo | Log source health (is the log file readable and growing) |
| [F2B-034](F2B-034.md) | P1 | 9 | todo | Failed-login reason breakdown from Frappe logs |
| [F2B-035](F2B-035.md) | P2 | 11 | todo | Trusted network profiles (office, VPN) managed with approval |
| [F2B-036](F2B-036.md) | P2 | 11 | todo | Temporary allow for a user's IP with auto-expiry and audit |
| [F2B-037](F2B-037.md) | P2 | 11 | todo | Repeat-offender report with suggestions |
| [F2B-038](F2B-038.md) | P2 | 11 | todo | Abuse-report export template (no automatic external submission) |
| [F2B-039](F2B-039.md) | P2 | 11 | todo | Integration test harness with a containerized fail2ban |
| [F2B-040](F2B-040.md) | P2 | 11 | todo | Alternative backends adapter interface (CrowdSec read-only status) for future |
