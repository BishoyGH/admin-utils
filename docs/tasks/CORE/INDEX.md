# CORE — Platform, Shell & Cross-Cutting: tasks

Spec: [`00-core-platform.md`](../../specs/00-core-platform.md) · 65 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [CORE-001](CORE-001.md) | P0 | 0 | todo | App registered in app switcher via `add_to_apps_screen` (v15 + v16 variants) |
| [CORE-002](CORE-002.md) | P0 | 0 | todo | SPA served at `/manage` with login redirect and role gate |
| [CORE-003](CORE-003.md) | P0 | 0 | todo | `Admin Utils Settings` single doctype with per-feature on/off toggles |
| [CORE-004](CORE-004.md) | P0 | 0 | todo | Role set + role profiles installed by fixtures/after_install |
| [CORE-005](CORE-005.md) | P0 | 0 | todo | Compatibility layer `core/compat.py` with v15/v16 implementations |
| [CORE-006](CORE-006.md) | P0 | 0 | todo | Central `guard()` decorator (role + feature flag + rate limit) |
| [CORE-007](CORE-007.md) | P0 | 0 | todo | Immutable `Admin Utils Audit Log` doctype (who/what/when/IP/before/after) |
| [CORE-008](CORE-008.md) | P0 | 0 | todo | Audit log viewer with filters, export, and diff view |
| [CORE-009](CORE-009.md) | P0 | 0 | todo | App shell: sidebar, top bar, breadcrumbs, responsive layout |
| [CORE-010](CORE-010.md) | P0 | 0 | todo | Lazy-loaded routes per feature module |
| [CORE-011](CORE-011.md) | P0 | 0 | todo | Global error boundary with friendly error + copyable trace id |
| [CORE-012](CORE-012.md) | P0 | 0 | todo | Standard API response envelope (`ok`, `data`, `error`, `trace_id`) |
| [CORE-013](CORE-013.md) | P0 | 0 | todo | Typed API client wrapper over frappe-ui `createResource` |
| [CORE-014](CORE-014.md) | P0 | 0 | todo | Background job framework (enqueue, status, cancel, retry) |
| [CORE-015](CORE-015.md) | P0 | 0 | todo | Realtime progress streaming for jobs (`publish_realtime`) |
| [CORE-016](CORE-016.md) | P0 | 0 | todo | Job center UI listing all jobs with logs |
| [CORE-017](CORE-017.md) | P1 | 0 | todo | Confirmation dialog component with typed-confirmation mode |
| [CORE-018](CORE-018.md) | P1 | 0 | todo | Global command palette (Ctrl/Cmd+K) to jump between utilities |
| [CORE-019](CORE-019.md) | P1 | 0 | todo | Global search across utilities, doctypes, roles, users |
| [CORE-020](CORE-020.md) | P1 | 0 | todo | Light/dark mode aware of Frappe desk theme |
| [CORE-021](CORE-021.md) | P0 | 0 | todo | Full RTL support with logical CSS properties |
| [CORE-022](CORE-022.md) | P0 | 0 | todo | i18n for UI strings (English + Arabic shipped) |
| [CORE-023](CORE-023.md) | P1 | 0 | todo | Per-user preferences store (table density, default landing page) |
| [CORE-024](CORE-024.md) | P1 | 0 | todo | Snapshot/Undo framework (generic before-state capture + restore) |
| [CORE-025](CORE-025.md) | P1 | 0 | todo | Preview/Diff component reused by all bulk-change features |
| [CORE-026](CORE-026.md) | P1 | 0 | todo | Reusable data table (virtualized, column chooser, sticky header) |
| [CORE-027](CORE-027.md) | P1 | 0 | todo | Reusable JSON editor/viewer with schema validation |
| [CORE-028](CORE-028.md) | P1 | 0 | todo | Reusable code editor (Monaco, lazy loaded) for Python/SQL/JSON |
| [CORE-029](CORE-029.md) | P1 | 0 | todo | Reusable tree component (modules → doctypes → fields) |
| [CORE-030](CORE-030.md) | P1 | 0 | todo | Reusable role/user/doctype pickers with async search |
| [CORE-031](CORE-031.md) | P1 | 0 | todo | Toast/notification system integrated with job results |
| [CORE-032](CORE-032.md) | P1 | 0 | todo | Keyboard shortcut system and shortcut help overlay |
| [CORE-033](CORE-033.md) | P1 | 0 | todo | Empty-state, skeleton and loading patterns standardized |
| [CORE-034](CORE-034.md) | P1 | 0 | todo | Feature-flag service (server-driven) exposed to frontend |
| [CORE-035](CORE-035.md) | P1 | 0 | todo | Rate limiter for mutating endpoints (per user, per feature) |
| [CORE-036](CORE-036.md) | P1 | 0 | todo | Secret masking utility used by logs, API and UI |
| [CORE-037](CORE-037.md) | P1 | 0 | todo | Structured logger with correlation id per request/job |
| [CORE-038](CORE-038.md) | P1 | 0 | todo | App health endpoint (`/api/method/admin_utils.api.health`) |
| [CORE-039](CORE-039.md) | P2 | 11 | todo | Onboarding tour for the app's own first run |
| [CORE-040](CORE-040.md) | P2 | 11 | todo | In-app documentation drawer with contextual help per page |
| [CORE-041](CORE-041.md) | P2 | 11 | todo | "What's new" changelog panel |
| [CORE-042](CORE-042.md) | P2 | 11 | todo | Export/import of all app settings as one JSON bundle |
| [CORE-043](CORE-043.md) | P2 | 11 | todo | Multi-site awareness banner (shows current site, environment label) |
| [CORE-044](CORE-044.md) | P2 | 11 | todo | Environment badge (dev/staging/prod) with extra confirmation on prod |
| [CORE-045](CORE-045.md) | P2 | 11 | todo | Telemetry opt-in (anonymous usage counts), off by default |

## Additional capabilities

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [CORE-046](CORE-046.md) | P1 | 0 | todo | Plugin architecture: each module registers routes, nav items, settings and permissions via a manifest |
| [CORE-047](CORE-047.md) | P1 | 0 | todo | Module manifest validator at install and migrate time |
| [CORE-048](CORE-048.md) | P1 | 0 | todo | Dependency resolver between modules (e.g. REPT needs PERM-029) |
| [CORE-049](CORE-049.md) | P1 | 0 | todo | Central permission catalog listing every action and the role that grants it |
| [CORE-050](CORE-050.md) | P1 | 0 | todo | Standard pagination, sorting and filter contract for all list endpoints |
| [CORE-051](CORE-051.md) | P1 | 0 | todo | Request validation schemas auto-exported as OpenAPI |
| [CORE-052](CORE-052.md) | P1 | 0 | todo | Idempotency keys for mutating API calls |
| [CORE-053](CORE-053.md) | P1 | 0 | todo | Optimistic concurrency (version stamps) on editable config records |
| [CORE-054](CORE-054.md) | P1 | 0 | todo | Unified "dangerous action" pattern (preview, typed confirm, audit, undo hint) |
| [CORE-055](CORE-055.md) | P1 | 0 | todo | Standard retry/backoff helper for transient failures |
| [CORE-056](CORE-056.md) | P1 | 0 | todo | Job priorities, queues and per-feature concurrency caps |
| [CORE-057](CORE-057.md) | P1 | 0 | todo | Job scheduling (run later, recurring) via a single scheduler abstraction |
| [CORE-058](CORE-058.md) | P1 | 0 | todo | Job results retention policy and cleanup |
| [CORE-059](CORE-059.md) | P2 | 11 | todo | Saved filters and column layouts for every table, per user |
| [CORE-060](CORE-060.md) | P2 | 11 | todo | Recent items and favorites in the shell |
| [CORE-061](CORE-061.md) | P2 | 11 | todo | Breadcrumb history and "back to where I was" |
| [CORE-062](CORE-062.md) | P2 | 11 | todo | Multi-tab safe state (BroadcastChannel sync) |
| [CORE-063](CORE-063.md) | P2 | 11 | todo | Offline-tolerant UI states (banner, queued actions where safe) |
| [CORE-064](CORE-064.md) | P2 | 11 | todo | Session-expiry handling with re-login modal that preserves work |
| [CORE-065](CORE-065.md) | P2 | 11 | todo | Print/export any table to CSV/XLSX/PDF from one shared component |
