---
code: BLDR
title: "App Builder & Customization Export"
number: 24
status: draft
privileged: true
depends_on: [CORE, BNCH]
code_path: admin_utils/builder/
frontend_path: frontend/src/features/builder/
tasks: docs/tasks/BLDR/INDEX.md
---

# Spec 24 — App Builder & Customization Export (`BLDR`)

## Purpose

turn on-site customizations into version-controlled, installable Frappe apps, so admins can promote work from the UI into code without touching a terminal. All generation runs through allowlisted bench commands and fixed templates, never free-form shell.

## Placement

- Python package: `admin_utils/builder/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/builder/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `App Builder & Customization Export Settings`; on/off flag `enable_builder` in `Admin Utils Settings` (**off by default**)
- Module instructions for agents: `admin_utils/builder/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 18 |
| P1 | 35 |
| P2 | 17 |

Waves: wave 6 (53), wave 11 (17)

## Prerequisites

- [`CORE`](00-core-platform.md) must provide what this module consumes before dependent tasks start
- [`BNCH`](03-bench-commands.md) must provide what this module consumes before dependent tasks start

## Feature groups

### App scaffolding

| ID | P | Wave | Task |
|---|---|---|---|
| [BLDR-001](../tasks/BLDR/BLDR-001.md) | P0 | 6 | App creation wizard that runs `bench new-app` through the allowlisted bench runner |
| [BLDR-002](../tasks/BLDR/BLDR-002.md) | P0 | 6 | Name validation (snake_case, reserved names, collision with installed/existing apps) |
| [BLDR-003](../tasks/BLDR/BLDR-003.md) | P0 | 6 | Metadata form: title, description, publisher, email, license, version, required apps |
| [BLDR-004](../tasks/BLDR/BLDR-004.md) | P0 | 6 | Version-aware scaffold templates (v15 and v16 layout differences handled by the compat layer) |
| [BLDR-005](../tasks/BLDR/BLDR-005.md) | P0 | 6 | File-tree preview of everything that will be created before any write |
| [BLDR-006](../tasks/BLDR/BLDR-006.md) | P0 | 6 | Generation runs as a background job with live logs and cancel |
| [BLDR-007](../tasks/BLDR/BLDR-007.md) | P0 | 6 | Dedicated role `Admin Utils App Builder` plus feature flag, off by default |
| [BLDR-008](../tasks/BLDR/BLDR-008.md) | P0 | 6 | Production guard: creating or installing apps is blocked unless the environment policy allows it |
| [BLDR-009](../tasks/BLDR/BLDR-009.md) | P0 | 6 | Full audit entry for every generated app, file written and command run |
| [BLDR-010](../tasks/BLDR/BLDR-010.md) | P1 | 6 | Module definition inside the new app (one or more modules, icons, colors) |
| [BLDR-011](../tasks/BLDR/BLDR-011.md) | P1 | 6 | Git initialization with branch name, `.gitignore` and first commit |
| [BLDR-012](../tasks/BLDR/BLDR-012.md) | P1 | 6 | Pre-commit config, linters and formatter config generation |
| [BLDR-013](../tasks/BLDR/BLDR-013.md) | P1 | 6 | README, LICENSE, CHANGELOG and CONTRIBUTING generation |
| [BLDR-014](../tasks/BLDR/BLDR-014.md) | P1 | 6 | CI workflow scaffold (lint, unit tests, install-on-bench test) for v15 and v16 |
| [BLDR-015](../tasks/BLDR/BLDR-015.md) | P1 | 6 | Test scaffold with a passing smoke test and a permissions test template |
| [BLDR-016](../tasks/BLDR/BLDR-016.md) | P1 | 6 | Frontend scaffold option (Vite + Vue + Frappe UI) for apps that need an SPA |
| [BLDR-017](../tasks/BLDR/BLDR-017.md) | P1 | 6 | Docker/devcontainer files option for reproducible development |
| [BLDR-018](../tasks/BLDR/BLDR-018.md) | P2 | 11 | Scaffold presets: "customizations only", "custom doctypes", "integration app", "reporting app", "SPA app" |
| [BLDR-019](../tasks/BLDR/BLDR-019.md) | P2 | 11 | Organization template repository support (your company's own scaffold with standards baked in) |
| [BLDR-020](../tasks/BLDR/BLDR-020.md) | P2 | 11 | Brand and header injection (copyright header, publisher info) from THEM brand kit |

### Customization export

| ID | P | Wave | Task |
|---|---|---|---|
| [BLDR-021](../tasks/BLDR/BLDR-021.md) | P0 | 6 | Export selector listing all exportable items (Custom Field, Property Setter, Custom DocPerm, Client/Server Script, Print Format, Workflow, Notification, Report, Workspace, Dashboard Chart, Number Card, Email Template, Letterhead, Role, Role Profile, Module Onboarding, Web Form, Translation, Webhook, Assignment Rule, Auto Repeat) |
| [BLDR-022](../tasks/BLDR/BLDR-022.md) | P0 | 6 | Target app picker (existing custom app or newly generated one) with writability check |
| [BLDR-023](../tasks/BLDR/BLDR-023.md) | P0 | 6 | Fixtures export with per-doctype filters that are written into `hooks.py` safely |
| [BLDR-024](../tasks/BLDR/BLDR-024.md) | P0 | 6 | Safe `hooks.py` editor (AST-based merge, never string-splice; preserves comments and formatting where possible) |
| [BLDR-025](../tasks/BLDR/BLDR-025.md) | P0 | 6 | Diff preview of every file to be added or changed in the target app |
| [BLDR-026](../tasks/BLDR/BLDR-026.md) | P0 | 6 | Idempotent re-export (running twice produces no diff) |
| [BLDR-027](../tasks/BLDR/BLDR-027.md) | P0 | 6 | Dependency detection (custom field needs its doctype's app, workflow needs roles and states) |
| [BLDR-028](../tasks/BLDR/BLDR-028.md) | P0 | 6 | Automatic inclusion of required dependencies with explanation |
| [BLDR-029](../tasks/BLDR/BLDR-029.md) | P0 | 6 | Conflict detection against files already in the target app |
| [BLDR-030](../tasks/BLDR/BLDR-030.md) | P1 | 6 | Export custom DocTypes to module folders as standard doctype JSON with controller stubs |
| [BLDR-031](../tasks/BLDR/BLDR-031.md) | P1 | 6 | Export Print Formats to standard files (HTML/JSON) in module folders |
| [BLDR-032](../tasks/BLDR/BLDR-032.md) | P1 | 6 | Export Reports (query and script) into standard report folders with filters and roles |
| [BLDR-033](../tasks/BLDR/BLDR-033.md) | P1 | 6 | Export Workspaces, Dashboard Charts and Number Cards into the module |
| [BLDR-034](../tasks/BLDR/BLDR-034.md) | P1 | 6 | Export Client Scripts to JS files and wire them via `doctype_js` hooks, with review gate |
| [BLDR-035](../tasks/BLDR/BLDR-035.md) | P1 | 6 | Export Server Scripts to reviewed Python modules and wire them via `doc_events`/API, never auto-run unreviewed code |
| [BLDR-036](../tasks/BLDR/BLDR-036.md) | P1 | 6 | Export permissions (Custom DocPerm and ladder matrix from PERM) as fixtures or as an install patch |
| [BLDR-037](../tasks/BLDR/BLDR-037.md) | P1 | 6 | Export role profiles, roles and workflow definitions with dependency ordering |
| [BLDR-038](../tasks/BLDR/BLDR-038.md) | P1 | 6 | Export translations (scoped ones from TRNS) into the app's translations folder |
| [BLDR-039](../tasks/BLDR/BLDR-039.md) | P1 | 6 | Export theme tokens and custom CSS as app assets (after the CSS-injection scan) |
| [BLDR-040](../tasks/BLDR/BLDR-040.md) | P1 | 6 | Export onboarding flows and custom HTML blocks |
| [BLDR-041](../tasks/BLDR/BLDR-041.md) | P1 | 6 | Export Enhanced View definitions (VIEW) and Automation rules (AUTO) as fixtures |
| [BLDR-042](../tasks/BLDR/BLDR-042.md) | P1 | 6 | Export seeder recipes and scenario packs (DATA) as demo-data fixtures |
| [BLDR-043](../tasks/BLDR/BLDR-043.md) | P1 | 6 | Patch generator: record data changes as an idempotent patch with `patches.txt` registration |
| [BLDR-044](../tasks/BLDR/BLDR-044.md) | P1 | 6 | Move a customization: export then remove from the site's database layer (opt-in, with snapshot) |
| [BLDR-045](../tasks/BLDR/BLDR-045.md) | P1 | 6 | Selection by tag, module, doctype, owner, modified-since, or saved selection set |
| [BLDR-046](../tasks/BLDR/BLDR-046.md) | P1 | 6 | Sensitive-data scan before export (secrets in scripts, emails, API keys, passwords in fixtures) |
| [BLDR-047](../tasks/BLDR/BLDR-047.md) | P1 | 6 | Exclusion rules (never export system-managed or site-specific records) |
| [BLDR-048](../tasks/BLDR/BLDR-048.md) | P1 | 6 | Export summary report with counts, warnings and skipped items |
| [BLDR-049](../tasks/BLDR/BLDR-049.md) | P2 | 11 | Export profiles saved per app (repeatable "export everything for Sales customizations") |
| [BLDR-050](../tasks/BLDR/BLDR-050.md) | P2 | 11 | Scheduled export that opens a draft change set for review rather than writing directly |

### Sync, drift and lifecycle

| ID | P | Wave | Task |
|---|---|---|---|
| [BLDR-051](../tasks/BLDR/BLDR-051.md) | P1 | 6 | Drift detector between site customizations and the app's exported files |
| [BLDR-052](../tasks/BLDR/BLDR-052.md) | P1 | 6 | "Pull" direction: import app files back to the site with preview |
| [BLDR-053](../tasks/BLDR/BLDR-053.md) | P1 | 6 | Install-app flow on a chosen site with pre-checks, backup, and rollback plan |
| [BLDR-054](../tasks/BLDR/BLDR-054.md) | P1 | 6 | Uninstall-app flow with orphan check, data impact preview and mandatory backup |
| [BLDR-055](../tasks/BLDR/BLDR-055.md) | P1 | 6 | Version bump and changelog entry generation from detected changes |
| [BLDR-056](../tasks/BLDR/BLDR-056.md) | P1 | 6 | App health check (hooks valid, imports resolve, fixtures load, patches run) in a temporary site or dry-run |
| [BLDR-057](../tasks/BLDR/BLDR-057.md) | P1 | 6 | Migration safety review (patch ordering, destructive operations flagged) |
| [BLDR-058](../tasks/BLDR/BLDR-058.md) | P1 | 6 | Generate unit and permission tests for exported customizations (links to TSTD) |
| [BLDR-059](../tasks/BLDR/BLDR-059.md) | P2 | 11 | Git integration: commit, branch, tag, push to configured remote with token stored securely |
| [BLDR-060](../tasks/BLDR/BLDR-060.md) | P2 | 11 | Pull-request creation with auto-generated description of exported changes |
| [BLDR-061](../tasks/BLDR/BLDR-061.md) | P2 | 11 | Release packaging as archive with checksum and signature |
| [BLDR-062](../tasks/BLDR/BLDR-062.md) | P2 | 11 | App bundle import on another site (offline transfer of an exported app) |
| [BLDR-063](../tasks/BLDR/BLDR-063.md) | P2 | 11 | Multi-app workspace: split customizations across several apps by module or ownership |
| [BLDR-064](../tasks/BLDR/BLDR-064.md) | P2 | 11 | Move items between custom apps with reference updates |
| [BLDR-065](../tasks/BLDR/BLDR-065.md) | P2 | 11 | Fork/clone an existing custom app under a new name |
| [BLDR-066](../tasks/BLDR/BLDR-066.md) | P2 | 11 | Compatibility matrix per app (tested on v15, v16) with badges |
| [BLDR-067](../tasks/BLDR/BLDR-067.md) | P2 | 11 | App dependency graph visualization |
| [BLDR-068](../tasks/BLDR/BLDR-068.md) | P2 | 11 | App inventory with owner, purpose, last export, last release, health |
| [BLDR-069](../tasks/BLDR/BLDR-069.md) | P2 | 11 | Deprecation helper (mark app items obsolete, generate removal patches) |
| [BLDR-070](../tasks/BLDR/BLDR-070.md) | P2 | 11 | Customization-to-code explainer (shows which UI customization became which file) |

## Tests

- generated apps install and pass their own CI on v15 and v16; re-export is idempotent (zero diff); AST-based `hooks.py` edits preserve unrelated content; the sensitive-data scan catches planted secrets; promote then rollback restores the exact prior state.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- Generated apps contain unreviewed or unsafe code: fixed templates, review gate for scripts, sensitive-data scan, sandboxed output dir
- App creation/installation on production: environment-policy block, approvals, mandatory backup, canary on a clone

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
