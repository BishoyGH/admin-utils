---
code: CORE
title: "Platform, Shell & Cross-Cutting"
number: 00
status: draft
privileged: false
depends_on: []
code_path: admin_utils/core/
frontend_path: frontend/src/features/core/
tasks: docs/tasks/CORE/INDEX.md
---

# Spec 00 — Platform, Shell & Cross-Cutting (`CORE`)

## Purpose

Platform, Shell & Cross-Cutting: see feature groups below.

## Placement

- Python package: `admin_utils/core/` with `api/` (thin), `services/` (logic), doctypes; version differences only via `core/compat`
- Frontend: `frontend/src/features/core/` (lazy route group, Vue 3 + frappe-ui + Tailwind, RTL-safe)
- Settings doctype: `Platform, Shell & Cross-Cutting Settings`; on/off flag `enable_core` in `Admin Utils Settings`
- Module instructions for agents: `admin_utils/core/AGENTS.md`

## Scope and non-goals

- In scope: the tasks listed below, nothing else; one task = one reviewable change.
- Non-goals: overriding core Frappe, writing outside this module's package except through published interfaces, any shell execution, any secret in logs.

## Priorities and waves

| Priority | Tasks |
|---|---|
| P0 | 18 |
| P1 | 33 |
| P2 | 14 |

Waves: wave 0 (51), wave 11 (14)

## Feature groups

### Core

| ID | P | Wave | Task |
|---|---|---|---|
| [CORE-001](../tasks/CORE/CORE-001.md) | P0 | 0 | App registered in app switcher via `add_to_apps_screen` (v15 + v16 variants) |
| [CORE-002](../tasks/CORE/CORE-002.md) | P0 | 0 | SPA served at `/manage` with login redirect and role gate |
| [CORE-003](../tasks/CORE/CORE-003.md) | P0 | 0 | `Admin Utils Settings` single doctype with per-feature on/off toggles |
| [CORE-004](../tasks/CORE/CORE-004.md) | P0 | 0 | Role set + role profiles installed by fixtures/after_install |
| [CORE-005](../tasks/CORE/CORE-005.md) | P0 | 0 | Compatibility layer `core/compat.py` with v15/v16 implementations |
| [CORE-006](../tasks/CORE/CORE-006.md) | P0 | 0 | Central `guard()` decorator (role + feature flag + rate limit) |
| [CORE-007](../tasks/CORE/CORE-007.md) | P0 | 0 | Immutable `Admin Utils Audit Log` doctype (who/what/when/IP/before/after) |
| [CORE-008](../tasks/CORE/CORE-008.md) | P0 | 0 | Audit log viewer with filters, export, and diff view |
| [CORE-009](../tasks/CORE/CORE-009.md) | P0 | 0 | App shell: sidebar, top bar, breadcrumbs, responsive layout |
| [CORE-010](../tasks/CORE/CORE-010.md) | P0 | 0 | Lazy-loaded routes per feature module |
| [CORE-011](../tasks/CORE/CORE-011.md) | P0 | 0 | Global error boundary with friendly error + copyable trace id |
| [CORE-012](../tasks/CORE/CORE-012.md) | P0 | 0 | Standard API response envelope (`ok`, `data`, `error`, `trace_id`) |
| [CORE-013](../tasks/CORE/CORE-013.md) | P0 | 0 | Typed API client wrapper over frappe-ui `createResource` |
| [CORE-014](../tasks/CORE/CORE-014.md) | P0 | 0 | Background job framework (enqueue, status, cancel, retry) |
| [CORE-015](../tasks/CORE/CORE-015.md) | P0 | 0 | Realtime progress streaming for jobs (`publish_realtime`) |
| [CORE-016](../tasks/CORE/CORE-016.md) | P0 | 0 | Job center UI listing all jobs with logs |
| [CORE-017](../tasks/CORE/CORE-017.md) | P1 | 0 | Confirmation dialog component with typed-confirmation mode |
| [CORE-018](../tasks/CORE/CORE-018.md) | P1 | 0 | Global command palette (Ctrl/Cmd+K) to jump between utilities |
| [CORE-019](../tasks/CORE/CORE-019.md) | P1 | 0 | Global search across utilities, doctypes, roles, users |
| [CORE-020](../tasks/CORE/CORE-020.md) | P1 | 0 | Light/dark mode aware of Frappe desk theme |
| [CORE-021](../tasks/CORE/CORE-021.md) | P0 | 0 | Full RTL support with logical CSS properties |
| [CORE-022](../tasks/CORE/CORE-022.md) | P0 | 0 | i18n for UI strings (English + Arabic shipped) |
| [CORE-023](../tasks/CORE/CORE-023.md) | P1 | 0 | Per-user preferences store (table density, default landing page) |
| [CORE-024](../tasks/CORE/CORE-024.md) | P1 | 0 | Snapshot/Undo framework (generic before-state capture + restore) |
| [CORE-025](../tasks/CORE/CORE-025.md) | P1 | 0 | Preview/Diff component reused by all bulk-change features |
| [CORE-026](../tasks/CORE/CORE-026.md) | P1 | 0 | Reusable data table (virtualized, column chooser, sticky header) |
| [CORE-027](../tasks/CORE/CORE-027.md) | P1 | 0 | Reusable JSON editor/viewer with schema validation |
| [CORE-028](../tasks/CORE/CORE-028.md) | P1 | 0 | Reusable code editor (Monaco, lazy loaded) for Python/SQL/JSON |
| [CORE-029](../tasks/CORE/CORE-029.md) | P1 | 0 | Reusable tree component (modules → doctypes → fields) |
| [CORE-030](../tasks/CORE/CORE-030.md) | P1 | 0 | Reusable role/user/doctype pickers with async search |
| [CORE-031](../tasks/CORE/CORE-031.md) | P1 | 0 | Toast/notification system integrated with job results |
| [CORE-032](../tasks/CORE/CORE-032.md) | P1 | 0 | Keyboard shortcut system and shortcut help overlay |
| [CORE-033](../tasks/CORE/CORE-033.md) | P1 | 0 | Empty-state, skeleton and loading patterns standardized |
| [CORE-034](../tasks/CORE/CORE-034.md) | P1 | 0 | Feature-flag service (server-driven) exposed to frontend |
| [CORE-035](../tasks/CORE/CORE-035.md) | P1 | 0 | Rate limiter for mutating endpoints (per user, per feature) |
| [CORE-036](../tasks/CORE/CORE-036.md) | P1 | 0 | Secret masking utility used by logs, API and UI |
| [CORE-037](../tasks/CORE/CORE-037.md) | P1 | 0 | Structured logger with correlation id per request/job |
| [CORE-038](../tasks/CORE/CORE-038.md) | P1 | 0 | App health endpoint (`/api/method/admin_utils.api.health`) |
| [CORE-039](../tasks/CORE/CORE-039.md) | P2 | 11 | Onboarding tour for the app's own first run |
| [CORE-040](../tasks/CORE/CORE-040.md) | P2 | 11 | In-app documentation drawer with contextual help per page |
| [CORE-041](../tasks/CORE/CORE-041.md) | P2 | 11 | "What's new" changelog panel |
| [CORE-042](../tasks/CORE/CORE-042.md) | P2 | 11 | Export/import of all app settings as one JSON bundle |
| [CORE-043](../tasks/CORE/CORE-043.md) | P2 | 11 | Multi-site awareness banner (shows current site, environment label) |
| [CORE-044](../tasks/CORE/CORE-044.md) | P2 | 11 | Environment badge (dev/staging/prod) with extra confirmation on prod |
| [CORE-045](../tasks/CORE/CORE-045.md) | P2 | 11 | Telemetry opt-in (anonymous usage counts), off by default |

### Additional capabilities

| ID | P | Wave | Task |
|---|---|---|---|
| [CORE-046](../tasks/CORE/CORE-046.md) | P1 | 0 | Plugin architecture: each module registers routes, nav items, settings and permissions via a manifest |
| [CORE-047](../tasks/CORE/CORE-047.md) | P1 | 0 | Module manifest validator at install and migrate time |
| [CORE-048](../tasks/CORE/CORE-048.md) | P1 | 0 | Dependency resolver between modules (e.g. REPT needs PERM-029) |
| [CORE-049](../tasks/CORE/CORE-049.md) | P1 | 0 | Central permission catalog listing every action and the role that grants it |
| [CORE-050](../tasks/CORE/CORE-050.md) | P1 | 0 | Standard pagination, sorting and filter contract for all list endpoints |
| [CORE-051](../tasks/CORE/CORE-051.md) | P1 | 0 | Request validation schemas auto-exported as OpenAPI |
| [CORE-052](../tasks/CORE/CORE-052.md) | P1 | 0 | Idempotency keys for mutating API calls |
| [CORE-053](../tasks/CORE/CORE-053.md) | P1 | 0 | Optimistic concurrency (version stamps) on editable config records |
| [CORE-054](../tasks/CORE/CORE-054.md) | P1 | 0 | Unified "dangerous action" pattern (preview, typed confirm, audit, undo hint) |
| [CORE-055](../tasks/CORE/CORE-055.md) | P1 | 0 | Standard retry/backoff helper for transient failures |
| [CORE-056](../tasks/CORE/CORE-056.md) | P1 | 0 | Job priorities, queues and per-feature concurrency caps |
| [CORE-057](../tasks/CORE/CORE-057.md) | P1 | 0 | Job scheduling (run later, recurring) via a single scheduler abstraction |
| [CORE-058](../tasks/CORE/CORE-058.md) | P1 | 0 | Job results retention policy and cleanup |
| [CORE-059](../tasks/CORE/CORE-059.md) | P2 | 11 | Saved filters and column layouts for every table, per user |
| [CORE-060](../tasks/CORE/CORE-060.md) | P2 | 11 | Recent items and favorites in the shell |
| [CORE-061](../tasks/CORE/CORE-061.md) | P2 | 11 | Breadcrumb history and "back to where I was" |
| [CORE-062](../tasks/CORE/CORE-062.md) | P2 | 11 | Multi-tab safe state (BroadcastChannel sync) |
| [CORE-063](../tasks/CORE/CORE-063.md) | P2 | 11 | Offline-tolerant UI states (banner, queued actions where safe) |
| [CORE-064](../tasks/CORE/CORE-064.md) | P2 | 11 | Session-expiry handling with re-login modal that preserves work |
| [CORE-065](../tasks/CORE/CORE-065.md) | P2 | 11 | Print/export any table to CSV/XLSX/PDF from one shared component |

## Tests

- No module-specific highlights beyond the shared strategy; follow the security matrix and Definition of Done.
- Always: authorization matrix per endpoint, audit-row assertions for mutating actions, v15 + v16 CI, LTR/RTL screenshots for UI.
- Shared strategy: [`../plan/05-testing-strategy.md`](../plan/05-testing-strategy.md)

## Risks that apply

- v15/v16 schema divergence: keep every difference inside core/compat
- Secrets leakage in logs/UI: central masking utility lives here

## Spec authoring checklist (Architect + Implementer, before code)

- [ ] API contracts in `docs/contracts/` (inputs, outputs, errors, permissions, rate limits)
- [ ] Doctype JSON and patches reviewed
- [ ] Permission matrix: role x endpoint x action
- [ ] Audit events and their before/after payloads
- [ ] i18n keys EN + AR; RTL considerations
- [ ] Test list agreed per task (unit, integration, e2e, security, a11y)
- [ ] Open questions resolved or recorded as ADRs
