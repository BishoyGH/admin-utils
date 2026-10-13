---
code: PERF
title: "Performance Center"
number: 30
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/performance/
frontend_path: frontend/src/features/performance/
tasks: docs/tasks/PERF/INDEX.md
---

# Spec 30 — Performance Center (`PERF`)

## Purpose

Performance Center: see feature groups below.

## Placement

- Python package: `admin_utils/performance/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/performance/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Performance Center Settings`; on/off flag `enable_performance` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/performance/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P1 | 11 |
| P2 | 19 |

Waves: wave 9 (11), wave 11 (19)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [PERF-001](../tasks/PERF/PERF-001.md) | P1 | 9 | Slow query analyzer with normalized fingerprints, counts and timings |
| [PERF-002](../tasks/PERF/PERF-002.md) | P1 | 9 | Missing/unused index advisor (suggestions only, never auto-applied) |
| [PERF-003](../tasks/PERF/PERF-003.md) | P1 | 9 | Report performance leaderboard with drill-down to the query |
| [PERF-004](../tasks/PERF/PERF-004.md) | P1 | 9 | Form load profiler (queries, scripts, link validations per open) |
| [PERF-005](../tasks/PERF/PERF-005.md) | P1 | 9 | Background job profiler (duration, memory, retries by job type) |
| [PERF-006](../tasks/PERF/PERF-006.md) | P1 | 9 | Cache effectiveness view (hit rates, hot keys, invalidation frequency) |
| [PERF-007](../tasks/PERF/PERF-007.md) | P1 | 9 | N+1 query pattern detector in custom code (sampled) |
| [PERF-008](../tasks/PERF/PERF-008.md) | P1 | 9 | Table size and growth analysis with archival candidates |
| [PERF-009](../tasks/PERF/PERF-009.md) | P1 | 9 | Doctype health scoring (field count, JSON blobs, indexes, child table volume) |
| [PERF-010](../tasks/PERF/PERF-010.md) | P1 | 9 | Server Script and Client Script cost estimates (calls per hour × duration) |
| [PERF-011](../tasks/PERF/PERF-011.md) | P1 | 9 | Slow endpoint list with sample requests (parameters redacted) |
| [PERF-012](../tasks/PERF/PERF-012.md) | P2 | 11 | Query plan viewer with plain-language explanation |
| [PERF-013](../tasks/PERF/PERF-013.md) | P2 | 11 | Lock wait and deadlock history viewer |
| [PERF-014](../tasks/PERF/PERF-014.md) | P2 | 11 | Autovacuum-style maintenance suggestions (analyze/optimize recommendations) |
| [PERF-015](../tasks/PERF/PERF-015.md) | P2 | 11 | Worker count and queue sizing recommendations |
| [PERF-016](../tasks/PERF/PERF-016.md) | P2 | 11 | Nginx/gunicorn setting review (read-only recommendations) |
| [PERF-017](../tasks/PERF/PERF-017.md) | P2 | 11 | Redis memory breakdown and eviction warnings |
| [PERF-018](../tasks/PERF/PERF-018.md) | P2 | 11 | Front-end performance budget tracker for the SPA (bundle sizes per release) |
| [PERF-019](../tasks/PERF/PERF-019.md) | P2 | 11 | Web vitals collection for the SPA (opt-in, aggregate) |
| [PERF-020](../tasks/PERF/PERF-020.md) | P2 | 11 | Seeded load test runner with before/after comparison |
| [PERF-021](../tasks/PERF/PERF-021.md) | P2 | 11 | Capacity model (users × documents × reports → resource needs) |
| [PERF-022](../tasks/PERF/PERF-022.md) | P2 | 11 | Regression detector comparing p95 latency before and after each release or change set |
| [PERF-023](../tasks/PERF/PERF-023.md) | P2 | 11 | Report materialization suggestions (heavy reports that should be cached) |
| [PERF-024](../tasks/PERF/PERF-024.md) | P2 | 11 | Archive-and-purge planner for logs, versions and email queue |
| [PERF-025](../tasks/PERF/PERF-025.md) | P2 | 11 | Pagination misuse finder (endpoints returning too many rows) |
| [PERF-026](../tasks/PERF/PERF-026.md) | P2 | 11 | Upload and attachment hot-spot report |
| [PERF-027](../tasks/PERF/PERF-027.md) | P2 | 11 | Scheduled performance digest |
| [PERF-028](../tasks/PERF/PERF-028.md) | P2 | 11 | Benchmark suite for common operations on a seeded dataset |
| [PERF-029](../tasks/PERF/PERF-029.md) | P2 | 11 | Performance budgets as policies in GOVN with violation alerts |
| [PERF-030](../tasks/PERF/PERF-030.md) | P2 | 11 | Tuning playbooks library with before/after evidence |

## Tests

- No module-specific highlights beyond the shared strategy; follow the security matrix and Definition of Done.
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
