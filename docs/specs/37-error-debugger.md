---
code: DBUG
title: "Error Debugger & Triage"
number: 37
status: draft
privileged: false
depends_on: [CORE, LOGS, DATA]
code_path: admin_utils/debugger/
frontend_path: frontend/src/features/debugger/
tasks: docs/tasks/DBUG/INDEX.md
---

# Spec 37 — Error Debugger & Triage (`DBUG`)

## Purpose

turn a raw error into an understood, owned and resolved problem: group, explain, reproduce, fix and verify.

## Placement

- Python package: `admin_utils/debugger/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/debugger/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Error Debugger & Triage Settings`; on/off flag `enable_debugger` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/debugger/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 7 |
| P1 | 39 |
| P2 | 24 |

Waves: wave 2 (46), wave 11 (24)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start
- [`LOGS`](36-log-center.md) must provide what this module consumes before dependent tasks start
- [`DATA`](09-data-seeder.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Triage & grouping

| ID | P | Wave | Task |
|---|---|---|---|
| [DBUG-001](../tasks/DBUG/DBUG-001.md) | P0 | 2 | Error inbox listing grouped errors with count, first seen, last seen, affected users and status |
| [DBUG-002](../tasks/DBUG/DBUG-002.md) | P0 | 2 | Fingerprinting that groups errors by exception type and normalized stack, ignoring volatile values |
| [DBUG-003](../tasks/DBUG/DBUG-003.md) | P0 | 2 | Error detail page: message, exception chain, stack trace, request context (masked), environment and version info |
| [DBUG-004](../tasks/DBUG/DBUG-004.md) | P0 | 2 | Status workflow (new, investigating, known issue, fixed, ignored) with owner and due date |
| [DBUG-005](../tasks/DBUG/DBUG-005.md) | P1 | 2 | Classification: expected validation message, permission denial, data integrity, timeout, resource, integration, code defect |
| [DBUG-006](../tasks/DBUG/DBUG-006.md) | P1 | 2 | Severity scoring from frequency, user impact, module criticality and trend |
| [DBUG-007](../tasks/DBUG/DBUG-007.md) | P1 | 2 | Assignment rules (route by app, module or doctype to an owner) |
| [DBUG-008](../tasks/DBUG/DBUG-008.md) | P1 | 2 | Reopen automatically when a "fixed" error returns after a later version |
| [DBUG-009](../tasks/DBUG/DBUG-009.md) | P1 | 2 | Merge and split groups manually when fingerprinting is wrong |
| [DBUG-010](../tasks/DBUG/DBUG-010.md) | P1 | 2 | Bulk actions (assign, ignore, resolve) with an undo window |
| [DBUG-011](../tasks/DBUG/DBUG-011.md) | P1 | 2 | Ignore rules with reason and expiry |
| [DBUG-012](../tasks/DBUG/DBUG-012.md) | P1 | 2 | Saved views (my errors, production-only, last release, security-related) |
| [DBUG-013](../tasks/DBUG/DBUG-013.md) | P2 | 11 | Related errors suggestion (similar fingerprint, shared cause) |
| [DBUG-014](../tasks/DBUG/DBUG-014.md) | P2 | 11 | Error budgets per module with breach alerts |
| [DBUG-015](../tasks/DBUG/DBUG-015.md) | P2 | 11 | Weekly triage digest with new, rising and stale items |

### Understanding the error

| ID | P | Wave | Task |
|---|---|---|---|
| [DBUG-016](../tasks/DBUG/DBUG-016.md) | P0 | 2 | Stack trace analyzer highlighting the first application frame and the likely responsible app |
| [DBUG-017](../tasks/DBUG/DBUG-017.md) | P0 | 2 | Request context panel (user, role, doctype, method, route, form values with sensitive fields masked, browser, IP) |
| [DBUG-018](../tasks/DBUG/DBUG-018.md) | P1 | 2 | "What changed before this" panel (recent change sets, config edits, permission applies, app updates, patches, backups, restarts) |
| [DBUG-019](../tasks/DBUG/DBUG-019.md) | P1 | 2 | First-seen correlation with releases and change markers |
| [DBUG-020](../tasks/DBUG/DBUG-020.md) | P1 | 2 | Affected-records view (which documents, users, companies hit the error) |
| [DBUG-021](../tasks/DBUG/DBUG-021.md) | P1 | 2 | Breakdown charts (by app, doctype, user, browser, version, hour) |
| [DBUG-022](../tasks/DBUG/DBUG-022.md) | P1 | 2 | Plain-language explanations for common Frappe errors (link validation, mandatory fields, naming conflicts, permission errors, deadlocks, timeouts, integrity errors) in EN/AR |
| [DBUG-023](../tasks/DBUG/DBUG-023.md) | P1 | 2 | Known-issues catalog with symptoms, causes and fixes, searchable and extensible by admins |
| [DBUG-024](../tasks/DBUG/DBUG-024.md) | P1 | 2 | Permission error debugger linked to the permission explainer (PERM-027) showing the exact rule that denied access |
| [DBUG-025](../tasks/DBUG/DBUG-025.md) | P1 | 2 | Validation error helper showing which field and which rule failed, with a link to the doctype definition |
| [DBUG-026](../tasks/DBUG/DBUG-026.md) | P1 | 2 | Database error helper (lock wait, deadlock, duplicate entry, data too long, missing column after migration) with next steps |
| [DBUG-027](../tasks/DBUG/DBUG-027.md) | P1 | 2 | Timeout and gateway error helper correlating 502/504 with worker, queue and database state at the same time |
| [DBUG-028](../tasks/DBUG/DBUG-028.md) | P1 | 2 | Memory and resource error helper correlating with MNTR metrics |
| [DBUG-029](../tasks/DBUG/DBUG-029.md) | P1 | 2 | Source viewer that shows code around a frame from installed apps, read-only, with the file path |
| [DBUG-030](../tasks/DBUG/DBUG-030.md) | P2 | 11 | Git blame and recent commit hints for the failing line when the app has a repository available |
| [DBUG-031](../tasks/DBUG/DBUG-031.md) | P2 | 11 | Dependency and version suspect list (library recently upgraded) |
| [DBUG-032](../tasks/DBUG/DBUG-032.md) | P2 | 11 | Client-side error capture from the app SPA and selected desk pages (opt-in, masked) with source-map support |
| [DBUG-033](../tasks/DBUG/DBUG-033.md) | P2 | 11 | Browser and device breakdown for client errors |
| [DBUG-034](../tasks/DBUG/DBUG-034.md) | P2 | 11 | Assistive explanation of a trace in plain language with human review (AIAS-006 extension) |

### Reproduce & fix

| ID | P | Wave | Task |
|---|---|---|---|
| [DBUG-035](../tasks/DBUG/DBUG-035.md) | P1 | 2 | Reproduction bundle export (sanitized request context, relevant records anonymized, versions, steps) for a developer |
| [DBUG-036](../tasks/DBUG/DBUG-036.md) | P1 | 2 | Sandbox reproduction: recreate the situation on a training or test site using seeded data |
| [DBUG-037](../tasks/DBUG/DBUG-037.md) | P1 | 2 | Safe replay of an allowlisted failed request against a test site (never against production) |
| [DBUG-038](../tasks/DBUG/DBUG-038.md) | P1 | 2 | Failed background job debugger: arguments (masked), queue history, retries, worker logs, one-click retry on a test site |
| [DBUG-039](../tasks/DBUG/DBUG-039.md) | P1 | 2 | Failed email debugger (queue entry, SMTP response, recipient validation, template render check) |
| [DBUG-040](../tasks/DBUG/DBUG-040.md) | P1 | 2 | Failed webhook and integration debugger with request, response, signature check and replay on a test endpoint |
| [DBUG-041](../tasks/DBUG/DBUG-041.md) | P1 | 2 | Failed patch and migration debugger (which patch, which statement, state of the schema, safe recovery guidance) |
| [DBUG-042](../tasks/DBUG/DBUG-042.md) | P1 | 2 | Failed import debugger (row-level reasons, corrected file generator) |
| [DBUG-043](../tasks/DBUG/DBUG-043.md) | P1 | 2 | Failed print/PDF debugger (template errors, missing fields, rendering engine output) |
| [DBUG-044](../tasks/DBUG/DBUG-044.md) | P1 | 2 | Scheduler and cron debugger (job never ran, ran twice, overlapped, stuck) |
| [DBUG-045](../tasks/DBUG/DBUG-045.md) | P1 | 2 | Workflow and approval debugger (why a transition is unavailable, which condition failed) |
| [DBUG-046](../tasks/DBUG/DBUG-046.md) | P1 | 2 | Server Script and Client Script error attribution (which script, which line, last edited by) |
| [DBUG-047](../tasks/DBUG/DBUG-047.md) | P2 | 11 | Generate a regression test from an error case (links TSTD) |
| [DBUG-048](../tasks/DBUG/DBUG-048.md) | P2 | 11 | Fix verification: after a fix is deployed, watch the fingerprint and confirm silence for a defined window |
| [DBUG-049](../tasks/DBUG/DBUG-049.md) | P2 | 11 | Hotfix helper that packages a fix as a change set through BLDR and MIGR |
| [DBUG-050](../tasks/DBUG/DBUG-050.md) | P2 | 11 | Rollback suggestion when an error appears right after a specific change set |

### Debug sessions

| ID | P | Wave | Task |
|---|---|---|---|
| [DBUG-051](../tasks/DBUG/DBUG-051.md) | P0 | 2 | Time-boxed debug session for one user or one doctype that raises log verbosity and captures extra context, expiring automatically |
| [DBUG-052](../tasks/DBUG/DBUG-052.md) | P1 | 2 | Verbose logging toggles for allowlisted loggers with auto-revert and audit |
| [DBUG-053](../tasks/DBUG/DBUG-053.md) | P1 | 2 | Capture-on-error snapshots (request, user, settings) stored with masking and short retention |
| [DBUG-054](../tasks/DBUG/DBUG-054.md) | P1 | 2 | "Ask the user to reproduce" flow: the user clicks a Record my session button, the admin receives a masked trace bundle |
| [DBUG-055](../tasks/DBUG/DBUG-055.md) | P1 | 2 | Developer-mode awareness (clear warnings when developer mode or debug settings are on in production) |
| [DBUG-056](../tasks/DBUG/DBUG-056.md) | P2 | 11 | Console for read-only diagnostic queries over an allowlist of safe diagnostics (never arbitrary code execution) |
| [DBUG-057](../tasks/DBUG/DBUG-057.md) | P2 | 11 | Variable inspector for captured frames with sensitive-name masking and size limits (opt-in, off by default) |
| [DBUG-058](../tasks/DBUG/DBUG-058.md) | P2 | 11 | Session recording of server-side events for one user flow (document events, hooks fired, permission checks) |

### Collaboration & reporting

| ID | P | Wave | Task |
|---|---|---|---|
| [DBUG-059](../tasks/DBUG/DBUG-059.md) | P1 | 2 | Comments, mentions and attachments on an error group |
| [DBUG-060](../tasks/DBUG/DBUG-060.md) | P1 | 2 | Create an issue draft for an external tracker (GitHub, GitLab or similar) with masked context, sent only after review |
| [DBUG-061](../tasks/DBUG/DBUG-061.md) | P1 | 2 | Link errors to change requests (GOVN) and releases |
| [DBUG-062](../tasks/DBUG/DBUG-062.md) | P2 | 11 | Incident declaration from an error group, linked to MNTR incidents |
| [DBUG-063](../tasks/DBUG/DBUG-063.md) | P2 | 11 | Post-mortem generator (timeline, impact, cause, fix, follow-ups) |
| [DBUG-064](../tasks/DBUG/DBUG-064.md) | P2 | 11 | MTTR and recurrence metrics by module and owner |
| [DBUG-065](../tasks/DBUG/DBUG-065.md) | P2 | 11 | Error-to-training loop: recurring user mistakes create suggested lessons (TRAIN, INSI) |
| [DBUG-066](../tasks/DBUG/DBUG-066.md) | P2 | 11 | Exportable error report (PDF, Markdown) for support or vendors, masked |
| [DBUG-067](../tasks/DBUG/DBUG-067.md) | P2 | 11 | Shareable read-only error link with expiry, scoped and audited |
| [DBUG-068](../tasks/DBUG/DBUG-068.md) | P2 | 11 | Vendor support bundle (versions, config summary, recent errors, health checks) with masking |
| [DBUG-069](../tasks/DBUG/DBUG-069.md) | P2 | 11 | Guided debugging walkthroughs for common problems (GUID flows) |
| [DBUG-070](../tasks/DBUG/DBUG-070.md) | P2 | 11 | Debugging knowledge base that grows from resolved errors (KNOW) |

## Tests

- parser tests against recorded fixtures for every supported format; multi-line and rotated-file handling; path-traversal and symlink attack tests; masking tests that plant secrets and personal data and assert they never reach the UI, exports or alerts; large-file performance tests; fingerprinting accuracy tests on a corpus of real-looking errors; reproduction-bundle sanitization tests; replay is refused against production-flagged environments; tracing overhead stays within budget under load.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Debug/replay causes real side effects: replay only on test sites, refuse production-flagged environments, no arbitrary code console
- Logs expose secrets: masking everywhere

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
