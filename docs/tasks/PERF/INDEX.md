# PERF — Performance Center: tasks

Spec: [`30-performance-center.md`](../../specs/30-performance-center.md) · 30 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [PERF-001](PERF-001.md) | P1 | 9 | todo | Slow query analyzer with normalized fingerprints, counts and timings |
| [PERF-002](PERF-002.md) | P1 | 9 | todo | Missing/unused index advisor (suggestions only, never auto-applied) |
| [PERF-003](PERF-003.md) | P1 | 9 | todo | Report performance leaderboard with drill-down to the query |
| [PERF-004](PERF-004.md) | P1 | 9 | todo | Form load profiler (queries, scripts, link validations per open) |
| [PERF-005](PERF-005.md) | P1 | 9 | todo | Background job profiler (duration, memory, retries by job type) |
| [PERF-006](PERF-006.md) | P1 | 9 | todo | Cache effectiveness view (hit rates, hot keys, invalidation frequency) |
| [PERF-007](PERF-007.md) | P1 | 9 | todo | N+1 query pattern detector in custom code (sampled) |
| [PERF-008](PERF-008.md) | P1 | 9 | todo | Table size and growth analysis with archival candidates |
| [PERF-009](PERF-009.md) | P1 | 9 | todo | Doctype health scoring (field count, JSON blobs, indexes, child table volume) |
| [PERF-010](PERF-010.md) | P1 | 9 | todo | Server Script and Client Script cost estimates (calls per hour × duration) |
| [PERF-011](PERF-011.md) | P1 | 9 | todo | Slow endpoint list with sample requests (parameters redacted) |
| [PERF-012](PERF-012.md) | P2 | 11 | todo | Query plan viewer with plain-language explanation |
| [PERF-013](PERF-013.md) | P2 | 11 | todo | Lock wait and deadlock history viewer |
| [PERF-014](PERF-014.md) | P2 | 11 | todo | Autovacuum-style maintenance suggestions (analyze/optimize recommendations) |
| [PERF-015](PERF-015.md) | P2 | 11 | todo | Worker count and queue sizing recommendations |
| [PERF-016](PERF-016.md) | P2 | 11 | todo | Nginx/gunicorn setting review (read-only recommendations) |
| [PERF-017](PERF-017.md) | P2 | 11 | todo | Redis memory breakdown and eviction warnings |
| [PERF-018](PERF-018.md) | P2 | 11 | todo | Front-end performance budget tracker for the SPA (bundle sizes per release) |
| [PERF-019](PERF-019.md) | P2 | 11 | todo | Web vitals collection for the SPA (opt-in, aggregate) |
| [PERF-020](PERF-020.md) | P2 | 11 | todo | Seeded load test runner with before/after comparison |
| [PERF-021](PERF-021.md) | P2 | 11 | todo | Capacity model (users × documents × reports → resource needs) |
| [PERF-022](PERF-022.md) | P2 | 11 | todo | Regression detector comparing p95 latency before and after each release or change set |
| [PERF-023](PERF-023.md) | P2 | 11 | todo | Report materialization suggestions (heavy reports that should be cached) |
| [PERF-024](PERF-024.md) | P2 | 11 | todo | Archive-and-purge planner for logs, versions and email queue |
| [PERF-025](PERF-025.md) | P2 | 11 | todo | Pagination misuse finder (endpoints returning too many rows) |
| [PERF-026](PERF-026.md) | P2 | 11 | todo | Upload and attachment hot-spot report |
| [PERF-027](PERF-027.md) | P2 | 11 | todo | Scheduled performance digest |
| [PERF-028](PERF-028.md) | P2 | 11 | todo | Benchmark suite for common operations on a seeded dataset |
| [PERF-029](PERF-029.md) | P2 | 11 | todo | Performance budgets as policies in GOVN with violation alerts |
| [PERF-030](PERF-030.md) | P2 | 11 | todo | Tuning playbooks library with before/after evidence |
