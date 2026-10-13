# LOGS — Log Center: tasks

Spec: [`36-log-center.md`](../../specs/36-log-center.md) · 90 tasks · done 0


## Sources & ingestion

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [LOGS-001](LOGS-001.md) | P0 | 2 | todo | Unified log explorer over database log doctypes (Error Log, Scheduled Job Log, Activity Log, Access Log, Email Queue and its errors, Integration Request, Webhook Request Log, Notification Log, Data Import Log, Submission Queue, Patch Log, Version, Comment, Deleted Document) |
| [LOGS-002](LOGS-002.md) | P0 | 2 | todo | Server file log viewer for the bench logs folder (web, worker, scheduler, frappe, socketio) with an allowlisted directory and path-traversal protection |
| [LOGS-003](LOGS-003.md) | P0 | 2 | todo | Source registry listing every available log source with status, size, last write and readability |
| [LOGS-004](LOGS-004.md) | P0 | 2 | todo | Live tail with pause, resume, auto-scroll and follow-new-lines |
| [LOGS-005](LOGS-005.md) | P0 | 2 | todo | Time-range picker with presets (last 15 minutes, hour, day, week) and absolute ranges |
| [LOGS-006](LOGS-006.md) | P0 | 2 | todo | Full-text search with highlighting across the selected sources |
| [LOGS-007](LOGS-007.md) | P0 | 2 | todo | Level filter (debug, info, warning, error, critical) with level detection for unstructured lines |
| [LOGS-008](LOGS-008.md) | P1 | 2 | todo | Reverse-proxy logs (nginx access and error) as read-only sources where the app has permission |
| [LOGS-009](LOGS-009.md) | P1 | 2 | todo | Database server logs (error log and slow query log) as read-only sources where available |
| [LOGS-010](LOGS-010.md) | P1 | 2 | todo | Process manager logs (supervisor or systemd journal) as read-only sources |
| [LOGS-011](LOGS-011.md) | P1 | 2 | todo | Redis and queue logs as read-only sources |
| [LOGS-012](LOGS-012.md) | P1 | 2 | todo | Fail2ban and authentication logs as read-only sources (links F2B) |
| [LOGS-013](LOGS-013.md) | P1 | 2 | todo | Backup and bench-command run logs (BNCH, BKUP) in the same explorer |
| [LOGS-014](LOGS-014.md) | P1 | 2 | todo | Logs from this app's modules (audit, jobs, exports, promotions, guidance) in the same explorer |
| [LOGS-015](LOGS-015.md) | P1 | 2 | todo | Custom app logger registration (other apps declare their log files and formats) |
| [LOGS-016](LOGS-016.md) | P1 | 2 | todo | Parser profiles for common formats (Python logging, gunicorn, nginx combined, MariaDB, JSON lines) with a profile editor and test box |
| [LOGS-017](LOGS-017.md) | P1 | 2 | todo | Multi-line entry joining (stack traces stay as one entry) |
| [LOGS-018](LOGS-018.md) | P1 | 2 | todo | Rotated and compressed file support (.1, .gz) with seamless paging |
| [LOGS-019](LOGS-019.md) | P1 | 2 | todo | Efficient large-file handling (indexed seek, chunked streaming, never loading whole files) |
| [LOGS-020](LOGS-020.md) | P2 | 11 | todo | Optional lightweight index store for fast search over retained history with configurable retention |
| [LOGS-021](LOGS-021.md) | P2 | 11 | todo | Multi-site bench view (select site or all sites) with per-site access control |
| [LOGS-022](LOGS-022.md) | P2 | 11 | todo | Remote source adapters (read-only) for centralized stores such as Loki, Elasticsearch or syslog, configured by admins |
| [LOGS-023](LOGS-023.md) | P2 | 11 | todo | Archive browser for old compressed logs with restore-to-view |

## Search & analysis

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [LOGS-024](LOGS-024.md) | P0 | 2 | todo | Structured filters (source, level, user, doctype, method, IP, status code, trace id) |
| [LOGS-025](LOGS-025.md) | P1 | 2 | todo | Query language with AND/OR/NOT, field filters, regex and time operators, plus a query builder UI |
| [LOGS-026](LOGS-026.md) | P1 | 2 | todo | Saved searches with names, owners, sharing and default time ranges |
| [LOGS-027](LOGS-027.md) | P1 | 2 | todo | Search history and quick re-run |
| [LOGS-028](LOGS-028.md) | P1 | 2 | todo | Context view (show N lines before and after a match, across sources by timestamp) |
| [LOGS-029](LOGS-029.md) | P1 | 2 | todo | Cross-source timeline: interleave web, worker, scheduler and database events in one time-ordered view |
| [LOGS-030](LOGS-030.md) | P1 | 2 | todo | Correlation by request id, trace id, job id and user session |
| [LOGS-031](LOGS-031.md) | P1 | 2 | todo | Pattern grouping (collapse similar lines into templates with counts) |
| [LOGS-032](LOGS-032.md) | P1 | 2 | todo | Top-N analysis (top errors, top endpoints, top users, top IPs, top slow requests) |
| [LOGS-033](LOGS-033.md) | P1 | 2 | todo | Volume histogram with level colors and click-to-zoom |
| [LOGS-034](LOGS-034.md) | P1 | 2 | todo | Compare two time ranges (before and after a release or change) |
| [LOGS-035](LOGS-035.md) | P1 | 2 | todo | Field extraction preview and custom field extraction rules with regex tester |
| [LOGS-036](LOGS-036.md) | P2 | 11 | todo | Statistical anomaly flags (sudden volume or error-rate changes) |
| [LOGS-037](LOGS-037.md) | P2 | 11 | todo | New-pattern detector (first-seen messages since the last release) |
| [LOGS-038](LOGS-038.md) | P2 | 11 | todo | Rare-event surfacing (messages that occur once in a long period) |
| [LOGS-039](LOGS-039.md) | P2 | 11 | todo | Pivot tables over extracted fields |
| [LOGS-040](LOGS-040.md) | P2 | 11 | todo | Bookmark and annotate lines, with notes shared in an investigation |
| [LOGS-041](LOGS-041.md) | P2 | 11 | todo | Investigation workspace: pin lines, searches, charts and notes into one shareable case |
| [LOGS-042](LOGS-042.md) | P2 | 11 | todo | Natural-language search drafting that produces a visible, editable query (assistive) |

## Reading experience

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [LOGS-043](LOGS-043.md) | P0 | 2 | todo | Readable entry detail panel with parsed fields, raw text, and copy buttons |
| [LOGS-044](LOGS-044.md) | P1 | 2 | todo | Syntax highlighting for JSON, SQL, stack traces and URLs |
| [LOGS-045](LOGS-045.md) | P1 | 2 | todo | Collapsible stack frames with application frames emphasized over library frames |
| [LOGS-046](LOGS-046.md) | P1 | 2 | todo | Timestamp handling (server timezone, user timezone, relative times, UTC toggle) |
| [LOGS-047](LOGS-047.md) | P1 | 2 | todo | Wrap, truncate and horizontal-scroll modes with a monospace font option |
| [LOGS-048](LOGS-048.md) | P1 | 2 | todo | Column chooser and density settings |
| [LOGS-049](LOGS-049.md) | P1 | 2 | todo | Keyboard navigation (next error, previous error, jump to time, open detail) |
| [LOGS-050](LOGS-050.md) | P1 | 2 | todo | Dark and light log themes that follow THEM tokens |
| [LOGS-051](LOGS-051.md) | P1 | 2 | todo | Arabic/RTL-safe layout (log text stays left-to-right, interface mirrors) |
| [LOGS-052](LOGS-052.md) | P2 | 11 | todo | Split view comparing two log sources or two time windows |
| [LOGS-053](LOGS-053.md) | P2 | 11 | todo | Mini-map and error markers on the scrollbar |
| [LOGS-054](LOGS-054.md) | P2 | 11 | todo | Mobile-friendly log reader for on-call use |

## Privacy, security & governance

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [LOGS-055](LOGS-055.md) | P0 | 2 | todo | Role gate `Admin Utils Log Viewer` with sub-permissions per source group (application, security, infrastructure) |
| [LOGS-056](LOGS-056.md) | P0 | 2 | todo | Masking at read time for secrets, tokens, passwords, API keys, session ids and configured personal-data patterns |
| [LOGS-057](LOGS-057.md) | P0 | 2 | todo | Audit entry for every log view, search, export and reveal-unmasked action |
| [LOGS-058](LOGS-058.md) | P1 | 2 | todo | Reveal-unmasked with re-authentication, reason and time-limited access |
| [LOGS-059](LOGS-059.md) | P1 | 2 | todo | Per-source retention policies with preview before purge |
| [LOGS-060](LOGS-060.md) | P1 | 2 | todo | Allowlist-only file access (no arbitrary paths) with symlink and traversal tests |
| [LOGS-061](LOGS-061.md) | P1 | 2 | todo | Export with masking and a size cap, as CSV, JSON lines or plain text, with watermark of who exported |
| [LOGS-062](LOGS-062.md) | P1 | 2 | todo | Scoped sharing of a saved search or investigation (viewer sees only what their role allows) |
| [LOGS-063](LOGS-063.md) | P2 | 11 | todo | Legal-hold flag preventing purge of selected ranges |
| [LOGS-064](LOGS-064.md) | P2 | 11 | todo | Tamper-evidence checks for audit-relevant logs (hash chain verification) |
| [LOGS-065](LOGS-065.md) | P2 | 11 | todo | Sensitive-data finder (reports where personal data or secrets appear in logs, so developers can stop logging it) |
| [LOGS-066](LOGS-066.md) | P2 | 11 | todo | Access review report (who viewed which logs and when) |

## Alerts, dashboards & automation

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [LOGS-067](LOGS-067.md) | P1 | 2 | todo | Log-based alert rules (pattern, threshold, rate, absence of an expected line) with severity and cooldown |
| [LOGS-068](LOGS-068.md) | P1 | 2 | todo | Alert routing through NTFY with the matching lines attached (masked) |
| [LOGS-069](LOGS-069.md) | P1 | 2 | todo | Log dashboard (errors per hour, top sources, slowest endpoints, failed jobs, login failures) |
| [LOGS-070](LOGS-070.md) | P1 | 2 | todo | Log health checks (source not writing, disk filling, rotation not happening, log level too verbose) |
| [LOGS-071](LOGS-071.md) | P1 | 2 | todo | Log level control for allowlisted loggers with time-boxed overrides that revert automatically |
| [LOGS-072](LOGS-072.md) | P2 | 11 | todo | Scheduled log digest (daily or weekly) with new patterns and top issues |
| [LOGS-073](LOGS-073.md) | P2 | 11 | todo | Absence alerts (the nightly job did not log completion) |
| [LOGS-074](LOGS-074.md) | P2 | 11 | todo | Log-to-metric rules (turn a pattern into a counter for MNTR charts) |
| [LOGS-075](LOGS-075.md) | P2 | 11 | todo | Auto-create a DBUG case from an alert |
| [LOGS-076](LOGS-076.md) | P2 | 11 | todo | Release markers and change markers overlaid on log histograms |
| [LOGS-077](LOGS-077.md) | P2 | 11 | todo | Noise suppression rules (known harmless messages) with owners and expiry |
| [LOGS-078](LOGS-078.md) | P2 | 11 | todo | Sampling controls for very chatty sources |
| [LOGS-079](LOGS-079.md) | P2 | 11 | todo | Cost and storage report for retained logs |

## Developer & integration

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [LOGS-080](LOGS-080.md) | P1 | 2 | todo | Logging standards checker (are custom apps using structured logs, correct levels, correlation ids) |
| [LOGS-081](LOGS-081.md) | P1 | 2 | todo | Structured logging helper library for custom apps (included in generated apps through BLDR) |
| [LOGS-082](LOGS-082.md) | P2 | 11 | todo | Log shipping configuration helper (read-only generator of config for external collectors) |
| [LOGS-083](LOGS-083.md) | P2 | 11 | todo | Query API for logs (permission-checked) for dashboards and external tools |
| [LOGS-084](LOGS-084.md) | P2 | 11 | todo | Webhook on matched patterns |
| [LOGS-085](LOGS-085.md) | P2 | 11 | todo | Logging coverage report per module (which actions emit logs) |
| [LOGS-086](LOGS-086.md) | P2 | 11 | todo | Logger inventory (all loggers in installed apps with levels and handlers) |
| [LOGS-087](LOGS-087.md) | P2 | 11 | todo | Test fixtures with sample logs for parser tests |
| [LOGS-088](LOGS-088.md) | P2 | 11 | todo | Parser plugin API for custom formats |
| [LOGS-089](LOGS-089.md) | P2 | 11 | todo | Log replay mode that feeds recorded logs into the explorer for training and demos (TRAIN scenarios) |
| [LOGS-090](LOGS-090.md) | P2 | 11 | todo | Training lessons on reading Frappe logs (TRAIN content pack) |
