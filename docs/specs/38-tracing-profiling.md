---
code: TRCE
title: "Tracing & Profiling"
number: 38
status: draft
privileged: false
depends_on: [CORE]
code_path: admin_utils/tracing/
frontend_path: frontend/src/features/tracing/
tasks: docs/tasks/TRCE/INDEX.md
---

# Spec 38 — Tracing & Profiling (`TRCE`)

## Purpose

see exactly what happened inside a slow or failing request or job: queries, hooks, cache calls and external requests in one timeline, with strict overhead limits.

## Placement

- Python package: `admin_utils/tracing/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/tracing/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Tracing & Profiling Settings`; on/off flag `enable_tracing` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/tracing/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 4 |
| P1 | 14 |
| P2 | 22 |

Waves: wave 0 (1), wave 9 (17), wave 11 (22)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [TRCE-001](../tasks/TRCE/TRCE-001.md) | P0 | 0 | Trace id generation and propagation (request → background job → email → webhook) |
| [TRCE-002](../tasks/TRCE/TRCE-002.md) | P0 | 9 | Trace store with sampling, size caps and short default retention |
| [TRCE-003](../tasks/TRCE/TRCE-003.md) | P0 | 9 | Overhead budget enforcement (automatic sampling reduction when overhead exceeds a threshold) |
| [TRCE-004](../tasks/TRCE/TRCE-004.md) | P0 | 9 | Request trace view: timeline of database queries, cache calls, hooks, external HTTP calls and render time |
| [TRCE-005](../tasks/TRCE/TRCE-005.md) | P1 | 9 | Slow-request auto-capture above a configurable threshold |
| [TRCE-006](../tasks/TRCE/TRCE-006.md) | P1 | 9 | SQL view inside a trace (normalized query, parameters masked, duration, rows, caller frame) |
| [TRCE-007](../tasks/TRCE/TRCE-007.md) | P1 | 9 | Duplicate and repeated query detection inside a trace (N+1 patterns) |
| [TRCE-008](../tasks/TRCE/TRCE-008.md) | P1 | 9 | Background job trace (enqueue time, queue wait, start, run, retries, result) |
| [TRCE-009](../tasks/TRCE/TRCE-009.md) | P1 | 9 | Document lifecycle trace (validate, before_save, on_update, on_submit hooks in order with timings) |
| [TRCE-010](../tasks/TRCE/TRCE-010.md) | P1 | 9 | Hook and event inventory showing which app handles which event, in which order, with costs |
| [TRCE-011](../tasks/TRCE/TRCE-011.md) | P1 | 9 | Permission check trace for a request (which rules were evaluated) |
| [TRCE-012](../tasks/TRCE/TRCE-012.md) | P1 | 9 | Workflow transition trace (conditions evaluated, roles checked, result) |
| [TRCE-013](../tasks/TRCE/TRCE-013.md) | P1 | 9 | Server Script execution trace (calls, duration, errors) |
| [TRCE-014](../tasks/TRCE/TRCE-014.md) | P1 | 9 | Link every trace to related log lines and error groups |
| [TRCE-015](../tasks/TRCE/TRCE-015.md) | P1 | 9 | Compare two traces (fast versus slow, before versus after a change) |
| [TRCE-016](../tasks/TRCE/TRCE-016.md) | P1 | 9 | Developer toolbar for authorized users (current page queries, timings and trace link), hidden unless enabled |
| [TRCE-017](../tasks/TRCE/TRCE-017.md) | P1 | 9 | SPA network waterfall (API calls, durations, payload sizes) with trace links |
| [TRCE-018](../tasks/TRCE/TRCE-018.md) | P1 | 9 | Trace redaction (parameters, headers, bodies masked by default) |
| [TRCE-019](../tasks/TRCE/TRCE-019.md) | P2 | 11 | On-demand time-boxed sampling profiler for allowlisted endpoints and jobs, with flame graph |
| [TRCE-020](../tasks/TRCE/TRCE-020.md) | P2 | 11 | Memory profiler snapshots (top allocations) time-boxed on test or staging by default |
| [TRCE-021](../tasks/TRCE/TRCE-021.md) | P2 | 11 | Realtime event trace (publish, deliver, drop) |
| [TRCE-022](../tasks/TRCE/TRCE-022.md) | P2 | 11 | Scheduler tick trace (which jobs were due, which ran, which skipped) |
| [TRCE-023](../tasks/TRCE/TRCE-023.md) | P2 | 11 | Cache trace (hits, misses, invalidations for a request) |
| [TRCE-024](../tasks/TRCE/TRCE-024.md) | P2 | 11 | External call trace (integrations, payment, SMS, email providers) with latency and error classification |
| [TRCE-025](../tasks/TRCE/TRCE-025.md) | P2 | 11 | Database lock trace for a transaction (waits, blockers) |
| [TRCE-026](../tasks/TRCE/TRCE-026.md) | P2 | 11 | Trace search (by user, doctype, endpoint, duration, status) |
| [TRCE-027](../tasks/TRCE/TRCE-027.md) | P2 | 11 | Trace sharing inside the admin team, scoped and audited |
| [TRCE-028](../tasks/TRCE/TRCE-028.md) | P2 | 11 | Export to OpenTelemetry format for external tools |
| [TRCE-029](../tasks/TRCE/TRCE-029.md) | P2 | 11 | Release comparison of latency distributions per endpoint |
| [TRCE-030](../tasks/TRCE/TRCE-030.md) | P2 | 11 | Synthetic trace runs from TSTD flows in test environments |
| [TRCE-031](../tasks/TRCE/TRCE-031.md) | P2 | 11 | Trace-driven performance budgets (PERF) with violation alerts |
| [TRCE-032](../tasks/TRCE/TRCE-032.md) | P2 | 11 | "Why was this slow?" guided diagnosis that ranks likely causes from the trace |
| [TRCE-033](../tasks/TRCE/TRCE-033.md) | P2 | 11 | Trace storage cost and retention dashboard |
| [TRCE-034](../tasks/TRCE/TRCE-034.md) | P2 | 11 | Per-user trace opt-in for support sessions with consent and expiry |
| [TRCE-035](../tasks/TRCE/TRCE-035.md) | P2 | 11 | Tracing hooks API for custom apps (declare spans for custom code) |
| [TRCE-036](../tasks/TRCE/TRCE-036.md) | P2 | 11 | Trace anomalies (sudden new slow span, new external dependency) |
| [TRCE-037](../tasks/TRCE/TRCE-037.md) | P2 | 11 | Client-side performance traces (long tasks, route transitions) in the SPA, opt-in |
| [TRCE-038](../tasks/TRCE/TRCE-038.md) | P2 | 11 | Trace fixtures for tests and training scenarios |
| [TRCE-039](../tasks/TRCE/TRCE-039.md) | P2 | 11 | Trace-based capacity hints (queries per request × traffic) |
| [TRCE-040](../tasks/TRCE/TRCE-040.md) | P2 | 11 | Training lessons on reading traces and fixing slow screens (TRAIN content pack) |

## Tests

- parser tests against recorded fixtures for every supported format; multi-line and rotated-file handling; path-traversal and symlink attack tests; masking tests that plant secrets and personal data and assert they never reach the UI, exports or alerts; large-file performance tests; fingerprinting accuracy tests on a corpus of real-looking errors; reproduction-bundle sanitization tests; replay is refused against production-flagged environments; tracing overhead stays within budget under load.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Tracing slows production: sampling, overhead budget with automatic back-off, time-boxed verbose modes
- Traces expose secrets: read-time masking

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
