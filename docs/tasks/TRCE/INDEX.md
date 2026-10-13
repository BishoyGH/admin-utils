# TRCE — Tracing & Profiling: tasks

Spec: [`38-tracing-profiling.md`](../../specs/38-tracing-profiling.md) · 40 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [TRCE-001](TRCE-001.md) | P0 | 0 | todo | Trace id generation and propagation (request → background job → email → webhook) |
| [TRCE-002](TRCE-002.md) | P0 | 9 | todo | Trace store with sampling, size caps and short default retention |
| [TRCE-003](TRCE-003.md) | P0 | 9 | todo | Overhead budget enforcement (automatic sampling reduction when overhead exceeds a threshold) |
| [TRCE-004](TRCE-004.md) | P0 | 9 | todo | Request trace view: timeline of database queries, cache calls, hooks, external HTTP calls and render time |
| [TRCE-005](TRCE-005.md) | P1 | 9 | todo | Slow-request auto-capture above a configurable threshold |
| [TRCE-006](TRCE-006.md) | P1 | 9 | todo | SQL view inside a trace (normalized query, parameters masked, duration, rows, caller frame) |
| [TRCE-007](TRCE-007.md) | P1 | 9 | todo | Duplicate and repeated query detection inside a trace (N+1 patterns) |
| [TRCE-008](TRCE-008.md) | P1 | 9 | todo | Background job trace (enqueue time, queue wait, start, run, retries, result) |
| [TRCE-009](TRCE-009.md) | P1 | 9 | todo | Document lifecycle trace (validate, before_save, on_update, on_submit hooks in order with timings) |
| [TRCE-010](TRCE-010.md) | P1 | 9 | todo | Hook and event inventory showing which app handles which event, in which order, with costs |
| [TRCE-011](TRCE-011.md) | P1 | 9 | todo | Permission check trace for a request (which rules were evaluated) |
| [TRCE-012](TRCE-012.md) | P1 | 9 | todo | Workflow transition trace (conditions evaluated, roles checked, result) |
| [TRCE-013](TRCE-013.md) | P1 | 9 | todo | Server Script execution trace (calls, duration, errors) |
| [TRCE-014](TRCE-014.md) | P1 | 9 | todo | Link every trace to related log lines and error groups |
| [TRCE-015](TRCE-015.md) | P1 | 9 | todo | Compare two traces (fast versus slow, before versus after a change) |
| [TRCE-016](TRCE-016.md) | P1 | 9 | todo | Developer toolbar for authorized users (current page queries, timings and trace link), hidden unless enabled |
| [TRCE-017](TRCE-017.md) | P1 | 9 | todo | SPA network waterfall (API calls, durations, payload sizes) with trace links |
| [TRCE-018](TRCE-018.md) | P1 | 9 | todo | Trace redaction (parameters, headers, bodies masked by default) |
| [TRCE-019](TRCE-019.md) | P2 | 11 | todo | On-demand time-boxed sampling profiler for allowlisted endpoints and jobs, with flame graph |
| [TRCE-020](TRCE-020.md) | P2 | 11 | todo | Memory profiler snapshots (top allocations) time-boxed on test or staging by default |
| [TRCE-021](TRCE-021.md) | P2 | 11 | todo | Realtime event trace (publish, deliver, drop) |
| [TRCE-022](TRCE-022.md) | P2 | 11 | todo | Scheduler tick trace (which jobs were due, which ran, which skipped) |
| [TRCE-023](TRCE-023.md) | P2 | 11 | todo | Cache trace (hits, misses, invalidations for a request) |
| [TRCE-024](TRCE-024.md) | P2 | 11 | todo | External call trace (integrations, payment, SMS, email providers) with latency and error classification |
| [TRCE-025](TRCE-025.md) | P2 | 11 | todo | Database lock trace for a transaction (waits, blockers) |
| [TRCE-026](TRCE-026.md) | P2 | 11 | todo | Trace search (by user, doctype, endpoint, duration, status) |
| [TRCE-027](TRCE-027.md) | P2 | 11 | todo | Trace sharing inside the admin team, scoped and audited |
| [TRCE-028](TRCE-028.md) | P2 | 11 | todo | Export to OpenTelemetry format for external tools |
| [TRCE-029](TRCE-029.md) | P2 | 11 | todo | Release comparison of latency distributions per endpoint |
| [TRCE-030](TRCE-030.md) | P2 | 11 | todo | Synthetic trace runs from TSTD flows in test environments |
| [TRCE-031](TRCE-031.md) | P2 | 11 | todo | Trace-driven performance budgets (PERF) with violation alerts |
| [TRCE-032](TRCE-032.md) | P2 | 11 | todo | "Why was this slow?" guided diagnosis that ranks likely causes from the trace |
| [TRCE-033](TRCE-033.md) | P2 | 11 | todo | Trace storage cost and retention dashboard |
| [TRCE-034](TRCE-034.md) | P2 | 11 | todo | Per-user trace opt-in for support sessions with consent and expiry |
| [TRCE-035](TRCE-035.md) | P2 | 11 | todo | Tracing hooks API for custom apps (declare spans for custom code) |
| [TRCE-036](TRCE-036.md) | P2 | 11 | todo | Trace anomalies (sudden new slow span, new external dependency) |
| [TRCE-037](TRCE-037.md) | P2 | 11 | todo | Client-side performance traces (long tasks, route transitions) in the SPA, opt-in |
| [TRCE-038](TRCE-038.md) | P2 | 11 | todo | Trace fixtures for tests and training scenarios |
| [TRCE-039](TRCE-039.md) | P2 | 11 | todo | Trace-based capacity hints (queries per request × traffic) |
| [TRCE-040](TRCE-040.md) | P2 | 11 | todo | Training lessons on reading traces and fixing slow screens (TRAIN content pack) |
