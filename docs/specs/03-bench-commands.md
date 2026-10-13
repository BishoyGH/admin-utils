---
code: BNCH
title: "Run Bench Commands From UI"
number: 03
status: draft
privileged: true
depends_on: [CORE]
code_path: admin_utils/bench/
frontend_path: frontend/src/features/bench/
tasks: docs/tasks/BNCH/INDEX.md
---

# Spec 03 — Run Bench Commands From UI (`BNCH`)

## Purpose

Run Bench Commands From UI: see feature groups below.

## Placement

- Python package: `admin_utils/bench/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/bench/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Run Bench Commands From UI Settings`; on/off flag `enable_bench` in `Admin Utils Settings` (**off by default**)
- Module instructions for agents: `admin_utils/bench/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 12 |
| P1 | 26 |
| P2 | 17 |

Waves: wave 4 (35), wave 9 (11), wave 11 (9)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [BNCH-001](../tasks/BNCH/BNCH-001.md) | P0 | 4 | Allowlist registry of permitted commands with argv templates |
| [BNCH-002](../tasks/BNCH/BNCH-002.md) | P0 | 4 | Per-command schema for arguments (type, range, regex) and validation |
| [BNCH-003](../tasks/BNCH/BNCH-003.md) | P0 | 4 | Execution via `subprocess` with `shell=False`, timeout, and resource limits |
| [BNCH-004](../tasks/BNCH/BNCH-004.md) | P0 | 4 | Run as background job with live stdout/stderr streaming |
| [BNCH-005](../tasks/BNCH/BNCH-005.md) | P0 | 4 | Role gate: `Admin Utils Bench Operator` only |
| [BNCH-006](../tasks/BNCH/BNCH-006.md) | P0 | 4 | Full audit log of command, args, user, exit code, duration |
| [BNCH-007](../tasks/BNCH/BNCH-007.md) | P0 | 4 | Typed confirmation for destructive commands |
| [BNCH-008](../tasks/BNCH/BNCH-008.md) | P0 | 4 | Global kill switch to disable the module entirely |
| [BNCH-009](../tasks/BNCH/BNCH-009.md) | P0 | 4 | `migrate` with pre-migrate backup option |
| [BNCH-010](../tasks/BNCH/BNCH-010.md) | P0 | 4 | `clear-cache`, `clear-website-cache` |
| [BNCH-011](../tasks/BNCH/BNCH-011.md) | P0 | 4 | `build` / `build --app` (where applicable) |
| [BNCH-012](../tasks/BNCH/BNCH-012.md) | P0 | 4 | `backup` (with/without files, compress) |
| [BNCH-013](../tasks/BNCH/BNCH-013.md) | P1 | 4 | `restart` via supervisor/systemd helper (configurable) |
| [BNCH-014](../tasks/BNCH/BNCH-014.md) | P1 | 4 | `doctor`, `show-config`, `list-apps` read-only info commands |
| [BNCH-015](../tasks/BNCH/BNCH-015.md) | P1 | 4 | `set-config` using key allowlist (links CONF module) |
| [BNCH-016](../tasks/BNCH/BNCH-016.md) | P1 | 4 | `reload-doctype`, `reload-doc` |
| [BNCH-017](../tasks/BNCH/BNCH-017.md) | P1 | 4 | `execute` limited to allowlisted dotted paths only |
| [BNCH-018](../tasks/BNCH/BNCH-018.md) | P1 | 4 | `export-fixtures`, `export-csv` |
| [BNCH-019](../tasks/BNCH/BNCH-019.md) | P1 | 4 | `scheduler enable/disable/status` |
| [BNCH-020](../tasks/BNCH/BNCH-020.md) | P1 | 4 | `set-maintenance-mode on/off` |
| [BNCH-021](../tasks/BNCH/BNCH-021.md) | P1 | 4 | Command presets ("Safe update", "Cache reset", "Nightly maintenance") |
| [BNCH-022](../tasks/BNCH/BNCH-022.md) | P1 | 4 | Multi-step runbooks (backup → migrate → clear cache → restart) with stop-on-failure |
| [BNCH-023](../tasks/BNCH/BNCH-023.md) | P1 | 4 | Dry-run/explain mode showing the exact argv to be executed |
| [BNCH-024](../tasks/BNCH/BNCH-024.md) | P1 | 4 | Output search, copy, download, and ANSI color rendering |
| [BNCH-025](../tasks/BNCH/BNCH-025.md) | P1 | 4 | Concurrency lock (one mutating command at a time per site) |
| [BNCH-026](../tasks/BNCH/BNCH-026.md) | P1 | 4 | Cancel running command safely (SIGTERM → SIGKILL) |
| [BNCH-027](../tasks/BNCH/BNCH-027.md) | P1 | 4 | Command history with re-run and compare |
| [BNCH-028](../tasks/BNCH/BNCH-028.md) | P2 | 4 | Scheduled commands (cron-like) with notifications |
| [BNCH-029](../tasks/BNCH/BNCH-029.md) | P2 | 4 | Pre-flight checks (disk space, pending backups, maintenance state) |
| [BNCH-030](../tasks/BNCH/BNCH-030.md) | P2 | 4 | Post-run health checks and auto-notify on failure |
| [BNCH-031](../tasks/BNCH/BNCH-031.md) | P2 | 4 | Approval step for production (second admin must approve) |
| [BNCH-032](../tasks/BNCH/BNCH-032.md) | P2 | 4 | Notify via email/Telegram/Slack webhook on completion |
| [BNCH-033](../tasks/BNCH/BNCH-033.md) | P2 | 4 | Custom command registration API for other apps (still allowlisted) |
| [BNCH-034](../tasks/BNCH/BNCH-034.md) | P2 | 4 | Per-environment command policies (dev allows more than prod) |
| [BNCH-035](../tasks/BNCH/BNCH-035.md) | P2 | 4 | Run summary report PDF for change management |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [BNCH-036](../tasks/BNCH/BNCH-036.md) | P1 | 9 | Command catalog UI with risk labels (read-only, mutating, destructive) |
| [BNCH-037](../tasks/BNCH/BNCH-037.md) | P1 | 9 | Per-command help with examples and expected side effects |
| [BNCH-038](../tasks/BNCH/BNCH-038.md) | P1 | 9 | Environment-aware defaults (e.g. skip build on prod unless asked) |
| [BNCH-039](../tasks/BNCH/BNCH-039.md) | P1 | 9 | Restart plan preview (which processes, expected downtime) |
| [BNCH-040](../tasks/BNCH/BNCH-040.md) | P1 | 9 | Maintenance banner auto-enable during risky runbooks |
| [BNCH-041](../tasks/BNCH/BNCH-041.md) | P1 | 9 | Runbook designer (ordered steps, conditions, retries, timeouts) |
| [BNCH-042](../tasks/BNCH/BNCH-042.md) | P1 | 9 | Runbook variables and parameter prompts at run time |
| [BNCH-043](../tasks/BNCH/BNCH-043.md) | P1 | 9 | Runbook dry-run executing only read-only steps |
| [BNCH-044](../tasks/BNCH/BNCH-044.md) | P1 | 9 | Step-level logs and resume-from-failed-step |
| [BNCH-045](../tasks/BNCH/BNCH-045.md) | P1 | 9 | Auto-rollback hooks (restore backup if migrate fails, opt-in) |
| [BNCH-046](../tasks/BNCH/BNCH-046.md) | P1 | 9 | Command output redaction of secrets and tokens |
| [BNCH-047](../tasks/BNCH/BNCH-047.md) | P2 | 11 | Bench/site selector when several sites exist, with per-site allowlists |
| [BNCH-048](../tasks/BNCH/BNCH-048.md) | P2 | 11 | Run history analytics (failure rate, avg duration) |
| [BNCH-049](../tasks/BNCH/BNCH-049.md) | P2 | 11 | Compare outputs of consecutive `migrate` runs (patches applied) |
| [BNCH-050](../tasks/BNCH/BNCH-050.md) | P2 | 11 | Disk-space-aware gating for backup/build |
| [BNCH-051](../tasks/BNCH/BNCH-051.md) | P2 | 11 | Calendar of scheduled operations with conflict detection |
| [BNCH-052](../tasks/BNCH/BNCH-052.md) | P2 | 11 | Hook points for pre/post command custom checks (allowlisted functions) |
| [BNCH-053](../tasks/BNCH/BNCH-053.md) | P2 | 11 | Export runbook as shell script for operators who prefer terminal (non-executing) |
| [BNCH-054](../tasks/BNCH/BNCH-054.md) | P2 | 11 | Signed runbooks (hash verified before run) |
| [BNCH-055](../tasks/BNCH/BNCH-055.md) | P2 | 11 | Two-person rule for runbooks marked "critical" |

## Tests

- argv construction snapshot tests, timeout/cancel tests, concurrency lock, no shell metacharacter ever reaches a shell; mocked `bench` binary in CI plus one real smoke job.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Bench misuse / RCE vector (critical): allowlist, argv lists, never a shell, sub-roles, off by default, pen-test

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
