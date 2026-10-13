---
code: F2B
title: "Fail2ban Integration"
number: 11
status: draft
privileged: true
depends_on: [CORE]
code_path: admin_utils/fail2ban/
frontend_path: frontend/src/features/fail2ban/
tasks: docs/tasks/F2B/INDEX.md
---

# Spec 11 — Fail2ban Integration (`F2B`)

## Purpose

Fail2ban Integration: see feature groups below.

## Placement

- Python package: `admin_utils/fail2ban/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/fail2ban/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Fail2ban Integration Settings`; on/off flag `enable_fail2ban` in `Admin Utils Settings` (**off by default**)
- Module instructions for agents: `admin_utils/fail2ban/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 8 |
| P1 | 17 |
| P2 | 15 |

Waves: wave 4 (21), wave 9 (4), wave 11 (15)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [F2B-001](../tasks/F2B/F2B-001.md) | P0 | 4 | Detect fail2ban installation, version and service state (read-only) |
| [F2B-002](../tasks/F2B/F2B-002.md) | P0 | 4 | Privileged helper design: minimal sudoers rule limited to specific `fail2ban-client` subcommands |
| [F2B-003](../tasks/F2B/F2B-003.md) | P0 | 4 | List jails and their status (currently failed/banned, totals) |
| [F2B-004](../tasks/F2B/F2B-004.md) | P0 | 4 | List banned IPs per jail with ban time |
| [F2B-005](../tasks/F2B/F2B-005.md) | P0 | 4 | Unban IP (validated IPv4/IPv6 only) with audit entry |
| [F2B-006](../tasks/F2B/F2B-006.md) | P0 | 4 | Manual ban IP with duration and reason |
| [F2B-007](../tasks/F2B/F2B-007.md) | P0 | 4 | Role gate `Admin Utils Security Admin` |
| [F2B-008](../tasks/F2B/F2B-008.md) | P0 | 4 | Safe-by-default: feature disabled until helper configured and verified |
| [F2B-009](../tasks/F2B/F2B-009.md) | P1 | 4 | Self-lockout protection (warn/block banning your own IP and allowlisted ranges) |
| [F2B-010](../tasks/F2B/F2B-010.md) | P1 | 4 | Whitelist (ignoreip) viewer and managed editor with backups |
| [F2B-011](../tasks/F2B/F2B-011.md) | P1 | 4 | Jail enable/disable for allowlisted jails |
| [F2B-012](../tasks/F2B/F2B-012.md) | P1 | 4 | Filter/jail config templates for Frappe login failures (nginx/access log pattern) |
| [F2B-013](../tasks/F2B/F2B-013.md) | P1 | 4 | Filter regex tester against sample log lines |
| [F2B-014](../tasks/F2B/F2B-014.md) | P1 | 4 | Ban log timeline and search (IP, jail, date) |
| [F2B-015](../tasks/F2B/F2B-015.md) | P1 | 4 | GeoIP info for banned IPs (local DB only, no external calls by default) |
| [F2B-016](../tasks/F2B/F2B-016.md) | P1 | 4 | Statistics (bans per day, top offenders, top jails) |
| [F2B-017](../tasks/F2B/F2B-017.md) | P1 | 4 | Link failed Frappe logins to bans (cross-reference Activity Log) |
| [F2B-018](../tasks/F2B/F2B-018.md) | P1 | 4 | Alerts when ban spikes occur |
| [F2B-019](../tasks/F2B/F2B-019.md) | P1 | 4 | Bulk unban and bulk ban from CSV with preview |
| [F2B-020](../tasks/F2B/F2B-020.md) | P1 | 4 | Reload fail2ban config safely with config test first |
| [F2B-021](../tasks/F2B/F2B-021.md) | P1 | 4 | Config backup/restore before any change |
| [F2B-022](../tasks/F2B/F2B-022.md) | P2 | 11 | Permanent ban list management (recidive jail view) |
| [F2B-023](../tasks/F2B/F2B-023.md) | P2 | 11 | Ban duration policy presets (progressive durations) |
| [F2B-024](../tasks/F2B/F2B-024.md) | P2 | 11 | Integration with Frappe rate-limit/login-attempt settings for consistent thresholds |
| [F2B-025](../tasks/F2B/F2B-025.md) | P2 | 11 | Notification on ban/unban events |
| [F2B-026](../tasks/F2B/F2B-026.md) | P2 | 11 | Export banned IP list |
| [F2B-027](../tasks/F2B/F2B-027.md) | P2 | 11 | Setup wizard generating install commands for the operator to run (not executed by app) |
| [F2B-028](../tasks/F2B/F2B-028.md) | P2 | 11 | Dry-run simulation of a filter on recent logs |
| [F2B-029](../tasks/F2B/F2B-029.md) | P2 | 11 | Optional nftables/iptables read-only status view |
| [F2B-030](../tasks/F2B/F2B-030.md) | P2 | 11 | Compatibility notes per distro (Ubuntu/Debian/Alma/Rocky) |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [F2B-031](../tasks/F2B/F2B-031.md) | P1 | 9 | Per-jail configuration viewer (maxretry, findtime, bantime) with human explanations |
| [F2B-032](../tasks/F2B/F2B-032.md) | P1 | 9 | Safe editing of selected jail parameters with validation and backup |
| [F2B-033](../tasks/F2B/F2B-033.md) | P1 | 9 | Log source health (is the log file readable and growing) |
| [F2B-034](../tasks/F2B/F2B-034.md) | P1 | 9 | Failed-login reason breakdown from Frappe logs |
| [F2B-035](../tasks/F2B/F2B-035.md) | P2 | 11 | Trusted network profiles (office, VPN) managed with approval |
| [F2B-036](../tasks/F2B/F2B-036.md) | P2 | 11 | Temporary allow for a user's IP with auto-expiry and audit |
| [F2B-037](../tasks/F2B/F2B-037.md) | P2 | 11 | Repeat-offender report with suggestions |
| [F2B-038](../tasks/F2B/F2B-038.md) | P2 | 11 | Abuse-report export template (no automatic external submission) |
| [F2B-039](../tasks/F2B/F2B-039.md) | P2 | 11 | Integration test harness with a containerized fail2ban |
| [F2B-040](../tasks/F2B/F2B-040.md) | P2 | 11 | Alternative backends adapter interface (CrowdSec read-only status) for future |

## Tests

- collectors tested with recorded fixtures; fail2ban client wrapped behind an interface and tested with a fake binary; real integration test in a container with fail2ban installed.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Bench/fail2ban misuse (critical): minimal sudoers rule limited to named fail2ban-client subcommands, off by default

## Privileged module gate

- Human approval on the **design** and on the **merge** (see `docs/checklists/privileged-review.md`).
- Security reviewer agent signs off; two reviewers; off by default behind a feature flag.
- Agents never receive production credentials; use disposable benches with seeded data.

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
