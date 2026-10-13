# MNTR — System Monitoring & Info: tasks

Spec: [`10-monitoring.md`](../../specs/10-monitoring.md) · 70 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [MNTR-001](MNTR-001.md) | P0 | 2 | todo | System overview: Frappe/ERPNext/app versions, Python, Node, MariaDB/Redis versions |
| [MNTR-002](MNTR-002.md) | P0 | 2 | todo | Site info: name, host, apps, developer mode, maintenance mode, scheduler state |
| [MNTR-003](MNTR-003.md) | P0 | 2 | todo | CPU, memory, swap, load average cards |
| [MNTR-004](MNTR-004.md) | P0 | 2 | todo | Disk usage per mount with threshold colors |
| [MNTR-005](MNTR-005.md) | P0 | 2 | todo | Database size, top tables by size, row counts |
| [MNTR-006](MNTR-006.md) | P0 | 2 | todo | Redis (cache/queue/socketio) status and memory |
| [MNTR-007](MNTR-007.md) | P0 | 2 | todo | Background worker/queue status (short/default/long) and depth |
| [MNTR-008](MNTR-008.md) | P0 | 2 | todo | Scheduler status and last-run per scheduled job |
| [MNTR-009](MNTR-009.md) | P0 | 2 | todo | Failed jobs list with retry/discard actions |
| [MNTR-010](MNTR-010.md) | P0 | 2 | todo | Error Log summary (counts by day, top errors) |
| [MNTR-011](MNTR-011.md) | P1 | 9 | todo | Active sessions/users now, last logins, failed login count |
| [MNTR-012](MNTR-012.md) | P1 | 9 | todo | Email queue status (pending/failed/sent) with retry |
| [MNTR-013](MNTR-013.md) | P1 | 9 | todo | Backup status: last backup time/size, retention, offsite status |
| [MNTR-014](MNTR-014.md) | P1 | 9 | todo | Slow query log viewer (when enabled) and index suggestions |
| [MNTR-015](MNTR-015.md) | P1 | 9 | todo | Request latency stats (p50/p95/p99) by endpoint |
| [MNTR-016](MNTR-016.md) | P1 | 9 | todo | Realtime/socketio connection health |
| [MNTR-017](MNTR-017.md) | P1 | 9 | todo | Log viewer (web, worker, scheduler, bench) with tail, search, download |
| [MNTR-018](MNTR-018.md) | P1 | 9 | todo | Service status (nginx, supervisor/systemd, redis, mariadb) read-only |
| [MNTR-019](MNTR-019.md) | P1 | 9 | todo | SSL certificate expiry check |
| [MNTR-020](MNTR-020.md) | P1 | 9 | todo | Time-series storage of metrics with retention policy |
| [MNTR-021](MNTR-021.md) | P1 | 9 | todo | Charts with selectable ranges (1h, 24h, 7d, 30d) |
| [MNTR-022](MNTR-022.md) | P1 | 9 | todo | Threshold-based alerts (email/Telegram/Slack) |
| [MNTR-023](MNTR-023.md) | P1 | 9 | todo | Alert rules editor with cooldown and severity |
| [MNTR-024](MNTR-024.md) | P1 | 9 | todo | Health check page with green/amber/red summary |
| [MNTR-025](MNTR-025.md) | P1 | 9 | todo | Public/uptime endpoint for external monitors (token protected) |
| [MNTR-026](MNTR-026.md) | P1 | 9 | todo | DB lock/long-running query viewer |
| [MNTR-027](MNTR-027.md) | P1 | 9 | todo | Storage usage: public/private files, orphan files detector |
| [MNTR-028](MNTR-028.md) | P1 | 9 | todo | Table growth trend (which doctypes grow fastest) |
| [MNTR-029](MNTR-029.md) | P1 | 9 | todo | Installed apps and pending patches list |
| [MNTR-030](MNTR-030.md) | P1 | 9 | todo | Security checklist (developer mode off, default passwords, 2FA coverage) |
| [MNTR-031](MNTR-031.md) | P2 | 11 | todo | Version update availability checker (read-only) |
| [MNTR-032](MNTR-032.md) | P2 | 11 | todo | Capacity forecast (disk/db growth projection) |
| [MNTR-033](MNTR-033.md) | P2 | 11 | todo | Per-user and per-doctype activity heatmap |
| [MNTR-034](MNTR-034.md) | P2 | 11 | todo | Scheduled health report email (weekly) |
| [MNTR-035](MNTR-035.md) | P2 | 11 | todo | Incident log (annotate outages and link to alerts) |
| [MNTR-036](MNTR-036.md) | P2 | 11 | todo | Prometheus-compatible metrics endpoint (token protected) |
| [MNTR-037](MNTR-037.md) | P2 | 11 | todo | Export diagnostics bundle (sanitized) for support |
| [MNTR-038](MNTR-038.md) | P2 | 11 | todo | Multi-site overview for benches hosting several sites |
| [MNTR-039](MNTR-039.md) | P2 | 11 | todo | Mobile-friendly monitoring dashboard |
| [MNTR-040](MNTR-040.md) | P2 | 11 | todo | Compare current metrics to a saved baseline |

## Additional capabilities

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [MNTR-041](MNTR-041.md) | P1 | 9 | todo | Per-queue throughput and wait-time charts |
| [MNTR-042](MNTR-042.md) | P1 | 9 | todo | Worker memory growth tracking |
| [MNTR-043](MNTR-043.md) | P1 | 9 | todo | Database connection pool usage and max-connection warnings |
| [MNTR-044](MNTR-044.md) | P1 | 9 | todo | InnoDB buffer pool and query cache style tuning hints (read-only advice) |
| [MNTR-045](MNTR-045.md) | P1 | 9 | todo | Table fragmentation and optimize suggestions |
| [MNTR-046](MNTR-046.md) | P1 | 9 | todo | Cron/scheduler lag detection |
| [MNTR-047](MNTR-047.md) | P1 | 9 | todo | Websocket error rates and reconnect stats |
| [MNTR-048](MNTR-048.md) | P1 | 9 | todo | Inbound/outbound email latency and bounce view |
| [MNTR-049](MNTR-049.md) | P1 | 9 | todo | Largest doctypes by attachment size |
| [MNTR-050](MNTR-050.md) | P1 | 9 | todo | Login heatmap by hour and failure geography (local GeoIP) |
| [MNTR-051](MNTR-051.md) | P2 | 11 | todo | Service-level objective definitions and burn-rate view |
| [MNTR-052](MNTR-052.md) | P2 | 11 | todo | Synthetic checks (login, load a list, run a report) with timings |
| [MNTR-053](MNTR-053.md) | P2 | 11 | todo | Error fingerprinting and grouping with first/last seen |
| [MNTR-054](MNTR-054.md) | P2 | 11 | todo | Release markers on charts (deploy events) |
| [MNTR-055](MNTR-055.md) | P2 | 11 | todo | Per-app resource attribution (best effort) |
| [MNTR-056](MNTR-056.md) | P2 | 11 | todo | Notification routing by severity and schedule (on-call hours) |
| [MNTR-057](MNTR-057.md) | P2 | 11 | todo | Maintenance windows that silence alerts |
| [MNTR-058](MNTR-058.md) | P2 | 11 | todo | Anomaly detection for sudden traffic or error spikes |
| [MNTR-059](MNTR-059.md) | P2 | 11 | todo | Cost-of-storage report (files, backups) |
| [MNTR-060](MNTR-060.md) | P2 | 11 | todo | Executive summary page (uptime, incidents, trends) exportable as PDF |

## Log-aware monitoring

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [MNTR-061](MNTR-061.md) | P1 | 9 | todo | One-click jump from any chart spike to the matching log range and error groups |
| [MNTR-062](MNTR-062.md) | P1 | 9 | todo | Log-derived metrics (error rate, failed jobs, login failures) as first-class MNTR charts |
| [MNTR-063](MNTR-063.md) | P1 | 9 | todo | Unified "what is wrong right now" panel combining failing checks, open alerts, top new errors and stuck jobs |
| [MNTR-064](MNTR-064.md) | P2 | 11 | todo | Service dependency map (web, workers, scheduler, redis, database, proxy) colored by health |
| [MNTR-065](MNTR-065.md) | P2 | 11 | todo | Error budget and availability view derived from logs and synthetic checks |
| [MNTR-066](MNTR-066.md) | P2 | 11 | todo | Rolling comparison against the same hour last week |
| [MNTR-067](MNTR-067.md) | P2 | 11 | todo | Health timeline showing when each check last changed state |
| [MNTR-068](MNTR-068.md) | P2 | 11 | todo | Slow-log summary cards for web, worker and database |
| [MNTR-069](MNTR-069.md) | P2 | 11 | todo | Job failure heatmap by job type and hour |
| [MNTR-070](MNTR-070.md) | P2 | 11 | todo | Operator view for wall screens combining health, alerts and top errors |
