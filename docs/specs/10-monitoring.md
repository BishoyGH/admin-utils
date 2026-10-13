---
code: MNTR
title: "System Monitoring & Info"
number: 10
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/monitoring/
frontend_path: frontend/src/features/monitoring/
tasks: docs/tasks/MNTR/INDEX.md
---

# Spec 10 — System Monitoring & Info (`MNTR`)

## Purpose

System Monitoring & Info: see feature groups below.

## Placement

- Python package: `admin_utils/monitoring/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/monitoring/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `System Monitoring & Info Settings`; on/off flag `enable_monitoring` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/monitoring/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 10 |
| P1 | 33 |
| P2 | 27 |

Waves: wave 2 (10), wave 9 (33), wave 11 (27)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [MNTR-001](../tasks/MNTR/MNTR-001.md) | P0 | 2 | System overview: Frappe/ERPNext/app versions, Python, Node, MariaDB/Redis versions |
| [MNTR-002](../tasks/MNTR/MNTR-002.md) | P0 | 2 | Site info: name, host, apps, developer mode, maintenance mode, scheduler state |
| [MNTR-003](../tasks/MNTR/MNTR-003.md) | P0 | 2 | CPU, memory, swap, load average cards |
| [MNTR-004](../tasks/MNTR/MNTR-004.md) | P0 | 2 | Disk usage per mount with threshold colors |
| [MNTR-005](../tasks/MNTR/MNTR-005.md) | P0 | 2 | Database size, top tables by size, row counts |
| [MNTR-006](../tasks/MNTR/MNTR-006.md) | P0 | 2 | Redis (cache/queue/socketio) status and memory |
| [MNTR-007](../tasks/MNTR/MNTR-007.md) | P0 | 2 | Background worker/queue status (short/default/long) and depth |
| [MNTR-008](../tasks/MNTR/MNTR-008.md) | P0 | 2 | Scheduler status and last-run per scheduled job |
| [MNTR-009](../tasks/MNTR/MNTR-009.md) | P0 | 2 | Failed jobs list with retry/discard actions |
| [MNTR-010](../tasks/MNTR/MNTR-010.md) | P0 | 2 | Error Log summary (counts by day, top errors) |
| [MNTR-011](../tasks/MNTR/MNTR-011.md) | P1 | 9 | Active sessions/users now, last logins, failed login count |
| [MNTR-012](../tasks/MNTR/MNTR-012.md) | P1 | 9 | Email queue status (pending/failed/sent) with retry |
| [MNTR-013](../tasks/MNTR/MNTR-013.md) | P1 | 9 | Backup status: last backup time/size, retention, offsite status |
| [MNTR-014](../tasks/MNTR/MNTR-014.md) | P1 | 9 | Slow query log viewer (when enabled) and index suggestions |
| [MNTR-015](../tasks/MNTR/MNTR-015.md) | P1 | 9 | Request latency stats (p50/p95/p99) by endpoint |
| [MNTR-016](../tasks/MNTR/MNTR-016.md) | P1 | 9 | Realtime/socketio connection health |
| [MNTR-017](../tasks/MNTR/MNTR-017.md) | P1 | 9 | Log viewer (web, worker, scheduler, bench) with tail, search, download |
| [MNTR-018](../tasks/MNTR/MNTR-018.md) | P1 | 9 | Service status (nginx, supervisor/systemd, redis, mariadb) read-only |
| [MNTR-019](../tasks/MNTR/MNTR-019.md) | P1 | 9 | SSL certificate expiry check |
| [MNTR-020](../tasks/MNTR/MNTR-020.md) | P1 | 9 | Time-series storage of metrics with retention policy |
| [MNTR-021](../tasks/MNTR/MNTR-021.md) | P1 | 9 | Charts with selectable ranges (1h, 24h, 7d, 30d) |
| [MNTR-022](../tasks/MNTR/MNTR-022.md) | P1 | 9 | Threshold-based alerts (email/Telegram/Slack) |
| [MNTR-023](../tasks/MNTR/MNTR-023.md) | P1 | 9 | Alert rules editor with cooldown and severity |
| [MNTR-024](../tasks/MNTR/MNTR-024.md) | P1 | 9 | Health check page with green/amber/red summary |
| [MNTR-025](../tasks/MNTR/MNTR-025.md) | P1 | 9 | Public/uptime endpoint for external monitors (token protected) |
| [MNTR-026](../tasks/MNTR/MNTR-026.md) | P1 | 9 | DB lock/long-running query viewer |
| [MNTR-027](../tasks/MNTR/MNTR-027.md) | P1 | 9 | Storage usage: public/private files, orphan files detector |
| [MNTR-028](../tasks/MNTR/MNTR-028.md) | P1 | 9 | Table growth trend (which doctypes grow fastest) |
| [MNTR-029](../tasks/MNTR/MNTR-029.md) | P1 | 9 | Installed apps and pending patches list |
| [MNTR-030](../tasks/MNTR/MNTR-030.md) | P1 | 9 | Security checklist (developer mode off, default passwords, 2FA coverage) |
| [MNTR-031](../tasks/MNTR/MNTR-031.md) | P2 | 11 | Version update availability checker (read-only) |
| [MNTR-032](../tasks/MNTR/MNTR-032.md) | P2 | 11 | Capacity forecast (disk/db growth projection) |
| [MNTR-033](../tasks/MNTR/MNTR-033.md) | P2 | 11 | Per-user and per-doctype activity heatmap |
| [MNTR-034](../tasks/MNTR/MNTR-034.md) | P2 | 11 | Scheduled health report email (weekly) |
| [MNTR-035](../tasks/MNTR/MNTR-035.md) | P2 | 11 | Incident log (annotate outages and link to alerts) |
| [MNTR-036](../tasks/MNTR/MNTR-036.md) | P2 | 11 | Prometheus-compatible metrics endpoint (token protected) |
| [MNTR-037](../tasks/MNTR/MNTR-037.md) | P2 | 11 | Export diagnostics bundle (sanitized) for support |
| [MNTR-038](../tasks/MNTR/MNTR-038.md) | P2 | 11 | Multi-site overview for benches hosting several sites |
| [MNTR-039](../tasks/MNTR/MNTR-039.md) | P2 | 11 | Mobile-friendly monitoring dashboard |
| [MNTR-040](../tasks/MNTR/MNTR-040.md) | P2 | 11 | Compare current metrics to a saved baseline |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [MNTR-041](../tasks/MNTR/MNTR-041.md) | P1 | 9 | Per-queue throughput and wait-time charts |
| [MNTR-042](../tasks/MNTR/MNTR-042.md) | P1 | 9 | Worker memory growth tracking |
| [MNTR-043](../tasks/MNTR/MNTR-043.md) | P1 | 9 | Database connection pool usage and max-connection warnings |
| [MNTR-044](../tasks/MNTR/MNTR-044.md) | P1 | 9 | InnoDB buffer pool and query cache style tuning hints (read-only advice) |
| [MNTR-045](../tasks/MNTR/MNTR-045.md) | P1 | 9 | Table fragmentation and optimize suggestions |
| [MNTR-046](../tasks/MNTR/MNTR-046.md) | P1 | 9 | Cron/scheduler lag detection |
| [MNTR-047](../tasks/MNTR/MNTR-047.md) | P1 | 9 | Websocket error rates and reconnect stats |
| [MNTR-048](../tasks/MNTR/MNTR-048.md) | P1 | 9 | Inbound/outbound email latency and bounce view |
| [MNTR-049](../tasks/MNTR/MNTR-049.md) | P1 | 9 | Largest doctypes by attachment size |
| [MNTR-050](../tasks/MNTR/MNTR-050.md) | P1 | 9 | Login heatmap by hour and failure geography (local GeoIP) |
| [MNTR-051](../tasks/MNTR/MNTR-051.md) | P2 | 11 | Service-level objective definitions and burn-rate view |
| [MNTR-052](../tasks/MNTR/MNTR-052.md) | P2 | 11 | Synthetic checks (login, load a list, run a report) with timings |
| [MNTR-053](../tasks/MNTR/MNTR-053.md) | P2 | 11 | Error fingerprinting and grouping with first/last seen |
| [MNTR-054](../tasks/MNTR/MNTR-054.md) | P2 | 11 | Release markers on charts (deploy events) |
| [MNTR-055](../tasks/MNTR/MNTR-055.md) | P2 | 11 | Per-app resource attribution (best effort) |
| [MNTR-056](../tasks/MNTR/MNTR-056.md) | P2 | 11 | Notification routing by severity and schedule (on-call hours) |
| [MNTR-057](../tasks/MNTR/MNTR-057.md) | P2 | 11 | Maintenance windows that silence alerts |
| [MNTR-058](../tasks/MNTR/MNTR-058.md) | P2 | 11 | Anomaly detection for sudden traffic or error spikes |
| [MNTR-059](../tasks/MNTR/MNTR-059.md) | P2 | 11 | Cost-of-storage report (files, backups) |
| [MNTR-060](../tasks/MNTR/MNTR-060.md) | P2 | 11 | Executive summary page (uptime, incidents, trends) exportable as PDF |

### Log-aware monitoring

| ID | P | Wave | Task |
|---|---|---|---|
| [MNTR-061](../tasks/MNTR/MNTR-061.md) | P1 | 9 | One-click jump from any chart spike to the matching log range and error groups |
| [MNTR-062](../tasks/MNTR/MNTR-062.md) | P1 | 9 | Log-derived metrics (error rate, failed jobs, login failures) as first-class MNTR charts |
| [MNTR-063](../tasks/MNTR/MNTR-063.md) | P1 | 9 | Unified "what is wrong right now" panel combining failing checks, open alerts, top new errors and stuck jobs |
| [MNTR-064](../tasks/MNTR/MNTR-064.md) | P2 | 11 | Service dependency map (web, workers, scheduler, redis, database, proxy) colored by health |
| [MNTR-065](../tasks/MNTR/MNTR-065.md) | P2 | 11 | Error budget and availability view derived from logs and synthetic checks |
| [MNTR-066](../tasks/MNTR/MNTR-066.md) | P2 | 11 | Rolling comparison against the same hour last week |
| [MNTR-067](../tasks/MNTR/MNTR-067.md) | P2 | 11 | Health timeline showing when each check last changed state |
| [MNTR-068](../tasks/MNTR/MNTR-068.md) | P2 | 11 | Slow-log summary cards for web, worker and database |
| [MNTR-069](../tasks/MNTR/MNTR-069.md) | P2 | 11 | Job failure heatmap by job type and hour |
| [MNTR-070](../tasks/MNTR/MNTR-070.md) | P2 | 11 | Operator view for wall screens combining health, alerts and top errors |

## Tests

- collectors tested with recorded fixtures; fail2ban client wrapped behind an interface and tested with a fake binary; real integration test in a container with fail2ban installed.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
