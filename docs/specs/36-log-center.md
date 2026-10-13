---
code: LOGS
title: "Log Center"
number: 36
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/logs/
frontend_path: frontend/src/features/logs/
tasks: docs/tasks/LOGS/INDEX.md
---

# Spec 36 — Log Center (`LOGS`)

## Purpose

one place to find, read, search and understand every kind of log a Frappe bench produces, from database log doctypes to server files, with strong privacy controls because logs often contain sensitive data.

## Placement

- Python package: `admin_utils/logs/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/logs/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Log Center Settings`; on/off flag `enable_logs` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/logs/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 12 |
| P1 | 43 |
| P2 | 35 |

Waves: wave 2 (55), wave 11 (35)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Sources & ingestion

| ID | P | Wave | Task |
|---|---|---|---|
| [LOGS-001](../tasks/LOGS/LOGS-001.md) | P0 | 2 | Unified log explorer over database log doctypes (Error Log, Scheduled Job Log, Activity Log, Access Log, Email Queue and its errors, Integration Request, Webhook Request Log, Notification Log, Data Import Log, Submission Queue, Patch Log, Version, Comment, Deleted Document) |
| [LOGS-002](../tasks/LOGS/LOGS-002.md) | P0 | 2 | Server file log viewer for the bench logs folder (web, worker, scheduler, frappe, socketio) with an allowlisted directory and path-traversal protection |
| [LOGS-003](../tasks/LOGS/LOGS-003.md) | P0 | 2 | Source registry listing every available log source with status, size, last write and readability |
| [LOGS-004](../tasks/LOGS/LOGS-004.md) | P0 | 2 | Live tail with pause, resume, auto-scroll and follow-new-lines |
| [LOGS-005](../tasks/LOGS/LOGS-005.md) | P0 | 2 | Time-range picker with presets (last 15 minutes, hour, day, week) and absolute ranges |
| [LOGS-006](../tasks/LOGS/LOGS-006.md) | P0 | 2 | Full-text search with highlighting across the selected sources |
| [LOGS-007](../tasks/LOGS/LOGS-007.md) | P0 | 2 | Level filter (debug, info, warning, error, critical) with level detection for unstructured lines |
| [LOGS-008](../tasks/LOGS/LOGS-008.md) | P1 | 2 | Reverse-proxy logs (nginx access and error) as read-only sources where the app has permission |
| [LOGS-009](../tasks/LOGS/LOGS-009.md) | P1 | 2 | Database server logs (error log and slow query log) as read-only sources where available |
| [LOGS-010](../tasks/LOGS/LOGS-010.md) | P1 | 2 | Process manager logs (supervisor or systemd journal) as read-only sources |
| [LOGS-011](../tasks/LOGS/LOGS-011.md) | P1 | 2 | Redis and queue logs as read-only sources |
| [LOGS-012](../tasks/LOGS/LOGS-012.md) | P1 | 2 | Fail2ban and authentication logs as read-only sources (links F2B) |
| [LOGS-013](../tasks/LOGS/LOGS-013.md) | P1 | 2 | Backup and bench-command run logs (BNCH, BKUP) in the same explorer |
| [LOGS-014](../tasks/LOGS/LOGS-014.md) | P1 | 2 | Logs from this app's modules (audit, jobs, exports, promotions, guidance) in the same explorer |
| [LOGS-015](../tasks/LOGS/LOGS-015.md) | P1 | 2 | Custom app logger registration (other apps declare their log files and formats) |
| [LOGS-016](../tasks/LOGS/LOGS-016.md) | P1 | 2 | Parser profiles for common formats (Python logging, gunicorn, nginx combined, MariaDB, JSON lines) with a profile editor and test box |
| [LOGS-017](../tasks/LOGS/LOGS-017.md) | P1 | 2 | Multi-line entry joining (stack traces stay as one entry) |
| [LOGS-018](../tasks/LOGS/LOGS-018.md) | P1 | 2 | Rotated and compressed file support (.1, .gz) with seamless paging |
| [LOGS-019](../tasks/LOGS/LOGS-019.md) | P1 | 2 | Efficient large-file handling (indexed seek, chunked streaming, never loading whole files) |
| [LOGS-020](../tasks/LOGS/LOGS-020.md) | P2 | 11 | Optional lightweight index store for fast search over retained history with configurable retention |
| [LOGS-021](../tasks/LOGS/LOGS-021.md) | P2 | 11 | Multi-site bench view (select site or all sites) with per-site access control |
| [LOGS-022](../tasks/LOGS/LOGS-022.md) | P2 | 11 | Remote source adapters (read-only) for centralized stores such as Loki, Elasticsearch or syslog, configured by admins |
| [LOGS-023](../tasks/LOGS/LOGS-023.md) | P2 | 11 | Archive browser for old compressed logs with restore-to-view |

### Search & analysis

| ID | P | Wave | Task |
|---|---|---|---|
| [LOGS-024](../tasks/LOGS/LOGS-024.md) | P0 | 2 | Structured filters (source, level, user, doctype, method, IP, status code, trace id) |
| [LOGS-025](../tasks/LOGS/LOGS-025.md) | P1 | 2 | Query language with AND/OR/NOT, field filters, regex and time operators, plus a query builder UI |
| [LOGS-026](../tasks/LOGS/LOGS-026.md) | P1 | 2 | Saved searches with names, owners, sharing and default time ranges |
| [LOGS-027](../tasks/LOGS/LOGS-027.md) | P1 | 2 | Search history and quick re-run |
| [LOGS-028](../tasks/LOGS/LOGS-028.md) | P1 | 2 | Context view (show N lines before and after a match, across sources by timestamp) |
| [LOGS-029](../tasks/LOGS/LOGS-029.md) | P1 | 2 | Cross-source timeline: interleave web, worker, scheduler and database events in one time-ordered view |
| [LOGS-030](../tasks/LOGS/LOGS-030.md) | P1 | 2 | Correlation by request id, trace id, job id and user session |
| [LOGS-031](../tasks/LOGS/LOGS-031.md) | P1 | 2 | Pattern grouping (collapse similar lines into templates with counts) |
| [LOGS-032](../tasks/LOGS/LOGS-032.md) | P1 | 2 | Top-N analysis (top errors, top endpoints, top users, top IPs, top slow requests) |
| [LOGS-033](../tasks/LOGS/LOGS-033.md) | P1 | 2 | Volume histogram with level colors and click-to-zoom |
| [LOGS-034](../tasks/LOGS/LOGS-034.md) | P1 | 2 | Compare two time ranges (before and after a release or change) |
| [LOGS-035](../tasks/LOGS/LOGS-035.md) | P1 | 2 | Field extraction preview and custom field extraction rules with regex tester |
| [LOGS-036](../tasks/LOGS/LOGS-036.md) | P2 | 11 | Statistical anomaly flags (sudden volume or error-rate changes) |
| [LOGS-037](../tasks/LOGS/LOGS-037.md) | P2 | 11 | New-pattern detector (first-seen messages since the last release) |
| [LOGS-038](../tasks/LOGS/LOGS-038.md) | P2 | 11 | Rare-event surfacing (messages that occur once in a long period) |
| [LOGS-039](../tasks/LOGS/LOGS-039.md) | P2 | 11 | Pivot tables over extracted fields |
| [LOGS-040](../tasks/LOGS/LOGS-040.md) | P2 | 11 | Bookmark and annotate lines, with notes shared in an investigation |
| [LOGS-041](../tasks/LOGS/LOGS-041.md) | P2 | 11 | Investigation workspace: pin lines, searches, charts and notes into one shareable case |
| [LOGS-042](../tasks/LOGS/LOGS-042.md) | P2 | 11 | Natural-language search drafting that produces a visible, editable query (assistive) |

### Reading experience

| ID | P | Wave | Task |
|---|---|---|---|
| [LOGS-043](../tasks/LOGS/LOGS-043.md) | P0 | 2 | Readable entry detail panel with parsed fields, raw text, and copy buttons |
| [LOGS-044](../tasks/LOGS/LOGS-044.md) | P1 | 2 | Syntax highlighting for JSON, SQL, stack traces and URLs |
| [LOGS-045](../tasks/LOGS/LOGS-045.md) | P1 | 2 | Collapsible stack frames with application frames emphasized over library frames |
| [LOGS-046](../tasks/LOGS/LOGS-046.md) | P1 | 2 | Timestamp handling (server timezone, user timezone, relative times, UTC toggle) |
| [LOGS-047](../tasks/LOGS/LOGS-047.md) | P1 | 2 | Wrap, truncate and horizontal-scroll modes with a monospace font option |
| [LOGS-048](../tasks/LOGS/LOGS-048.md) | P1 | 2 | Column chooser and density settings |
| [LOGS-049](../tasks/LOGS/LOGS-049.md) | P1 | 2 | Keyboard navigation (next error, previous error, jump to time, open detail) |
| [LOGS-050](../tasks/LOGS/LOGS-050.md) | P1 | 2 | Dark and light log themes that follow THEM tokens |
| [LOGS-051](../tasks/LOGS/LOGS-051.md) | P1 | 2 | Arabic/RTL-safe layout (log text stays left-to-right, interface mirrors) |
| [LOGS-052](../tasks/LOGS/LOGS-052.md) | P2 | 11 | Split view comparing two log sources or two time windows |
| [LOGS-053](../tasks/LOGS/LOGS-053.md) | P2 | 11 | Mini-map and error markers on the scrollbar |
| [LOGS-054](../tasks/LOGS/LOGS-054.md) | P2 | 11 | Mobile-friendly log reader for on-call use |

### Privacy, security & governance

| ID | P | Wave | Task |
|---|---|---|---|
| [LOGS-055](../tasks/LOGS/LOGS-055.md) | P0 | 2 | Role gate `Admin Utils Log Viewer` with sub-permissions per source group (application, security, infrastructure) |
| [LOGS-056](../tasks/LOGS/LOGS-056.md) | P0 | 2 | Masking at read time for secrets, tokens, passwords, API keys, session ids and configured personal-data patterns |
| [LOGS-057](../tasks/LOGS/LOGS-057.md) | P0 | 2 | Audit entry for every log view, search, export and reveal-unmasked action |
| [LOGS-058](../tasks/LOGS/LOGS-058.md) | P1 | 2 | Reveal-unmasked with re-authentication, reason and time-limited access |
| [LOGS-059](../tasks/LOGS/LOGS-059.md) | P1 | 2 | Per-source retention policies with preview before purge |
| [LOGS-060](../tasks/LOGS/LOGS-060.md) | P1 | 2 | Allowlist-only file access (no arbitrary paths) with symlink and traversal tests |
| [LOGS-061](../tasks/LOGS/LOGS-061.md) | P1 | 2 | Export with masking and a size cap, as CSV, JSON lines or plain text, with watermark of who exported |
| [LOGS-062](../tasks/LOGS/LOGS-062.md) | P1 | 2 | Scoped sharing of a saved search or investigation (viewer sees only what their role allows) |
| [LOGS-063](../tasks/LOGS/LOGS-063.md) | P2 | 11 | Legal-hold flag preventing purge of selected ranges |
| [LOGS-064](../tasks/LOGS/LOGS-064.md) | P2 | 11 | Tamper-evidence checks for audit-relevant logs (hash chain verification) |
| [LOGS-065](../tasks/LOGS/LOGS-065.md) | P2 | 11 | Sensitive-data finder (reports where personal data or secrets appear in logs, so developers can stop logging it) |
| [LOGS-066](../tasks/LOGS/LOGS-066.md) | P2 | 11 | Access review report (who viewed which logs and when) |

### Alerts, dashboards & automation

| ID | P | Wave | Task |
|---|---|---|---|
| [LOGS-067](../tasks/LOGS/LOGS-067.md) | P1 | 2 | Log-based alert rules (pattern, threshold, rate, absence of an expected line) with severity and cooldown |
| [LOGS-068](../tasks/LOGS/LOGS-068.md) | P1 | 2 | Alert routing through NTFY with the matching lines attached (masked) |
| [LOGS-069](../tasks/LOGS/LOGS-069.md) | P1 | 2 | Log dashboard (errors per hour, top sources, slowest endpoints, failed jobs, login failures) |
| [LOGS-070](../tasks/LOGS/LOGS-070.md) | P1 | 2 | Log health checks (source not writing, disk filling, rotation not happening, log level too verbose) |
| [LOGS-071](../tasks/LOGS/LOGS-071.md) | P1 | 2 | Log level control for allowlisted loggers with time-boxed overrides that revert automatically |
| [LOGS-072](../tasks/LOGS/LOGS-072.md) | P2 | 11 | Scheduled log digest (daily or weekly) with new patterns and top issues |
| [LOGS-073](../tasks/LOGS/LOGS-073.md) | P2 | 11 | Absence alerts (the nightly job did not log completion) |
| [LOGS-074](../tasks/LOGS/LOGS-074.md) | P2 | 11 | Log-to-metric rules (turn a pattern into a counter for MNTR charts) |
| [LOGS-075](../tasks/LOGS/LOGS-075.md) | P2 | 11 | Auto-create a DBUG case from an alert |
| [LOGS-076](../tasks/LOGS/LOGS-076.md) | P2 | 11 | Release markers and change markers overlaid on log histograms |
| [LOGS-077](../tasks/LOGS/LOGS-077.md) | P2 | 11 | Noise suppression rules (known harmless messages) with owners and expiry |
| [LOGS-078](../tasks/LOGS/LOGS-078.md) | P2 | 11 | Sampling controls for very chatty sources |
| [LOGS-079](../tasks/LOGS/LOGS-079.md) | P2 | 11 | Cost and storage report for retained logs |

### Developer & integration

| ID | P | Wave | Task |
|---|---|---|---|
| [LOGS-080](../tasks/LOGS/LOGS-080.md) | P1 | 2 | Logging standards checker (are custom apps using structured logs, correct levels, correlation ids) |
| [LOGS-081](../tasks/LOGS/LOGS-081.md) | P1 | 2 | Structured logging helper library for custom apps (included in generated apps through BLDR) |
| [LOGS-082](../tasks/LOGS/LOGS-082.md) | P2 | 11 | Log shipping configuration helper (read-only generator of config for external collectors) |
| [LOGS-083](../tasks/LOGS/LOGS-083.md) | P2 | 11 | Query API for logs (permission-checked) for dashboards and external tools |
| [LOGS-084](../tasks/LOGS/LOGS-084.md) | P2 | 11 | Webhook on matched patterns |
| [LOGS-085](../tasks/LOGS/LOGS-085.md) | P2 | 11 | Logging coverage report per module (which actions emit logs) |
| [LOGS-086](../tasks/LOGS/LOGS-086.md) | P2 | 11 | Logger inventory (all loggers in installed apps with levels and handlers) |
| [LOGS-087](../tasks/LOGS/LOGS-087.md) | P2 | 11 | Test fixtures with sample logs for parser tests |
| [LOGS-088](../tasks/LOGS/LOGS-088.md) | P2 | 11 | Parser plugin API for custom formats |
| [LOGS-089](../tasks/LOGS/LOGS-089.md) | P2 | 11 | Log replay mode that feeds recorded logs into the explorer for training and demos (TRAIN scenarios) |
| [LOGS-090](../tasks/LOGS/LOGS-090.md) | P2 | 11 | Training lessons on reading Frappe logs (TRAIN content pack) |

## Tests

- parser tests against recorded fixtures for every supported format; multi-line and rotated-file handling; path-traversal and symlink attack tests; masking tests that plant secrets and personal data and assert they never reach the UI, exports or alerts; large-file performance tests; fingerprinting accuracy tests on a corpus of real-looking errors; reproduction-bundle sanitization tests; replay is refused against production-flagged environments; tracing overhead stays within budget under load.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Logs expose secrets or personal data: read-time masking, role gates per source group, audited reveal with re-authentication, export watermarking
- Log tooling slows production: sampling, overhead budget, bounded reads

## Sensitive data

- Masking happens centrally at read time; tests plant secrets/personal data and assert they never reach UI, exports, alerts or AI providers.

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
