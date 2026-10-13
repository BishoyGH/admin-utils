# BLDR — App Builder & Customization Export: tasks

Spec: [`24-app-builder.md`](../../specs/24-app-builder.md) · 70 tasks · done 0


## App scaffolding

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [BLDR-001](BLDR-001.md) | P0 | 6 | todo | App creation wizard that runs `bench new-app` through the allowlisted bench runner |
| [BLDR-002](BLDR-002.md) | P0 | 6 | todo | Name validation (snake_case, reserved names, collision with installed/existing apps) |
| [BLDR-003](BLDR-003.md) | P0 | 6 | todo | Metadata form: title, description, publisher, email, license, version, required apps |
| [BLDR-004](BLDR-004.md) | P0 | 6 | todo | Version-aware scaffold templates (v15 and v16 layout differences handled by the compat layer) |
| [BLDR-005](BLDR-005.md) | P0 | 6 | todo | File-tree preview of everything that will be created before any write |
| [BLDR-006](BLDR-006.md) | P0 | 6 | todo | Generation runs as a background job with live logs and cancel |
| [BLDR-007](BLDR-007.md) | P0 | 6 | todo | Dedicated role `Admin Utils App Builder` plus feature flag, off by default |
| [BLDR-008](BLDR-008.md) | P0 | 6 | todo | Production guard: creating or installing apps is blocked unless the environment policy allows it |
| [BLDR-009](BLDR-009.md) | P0 | 6 | todo | Full audit entry for every generated app, file written and command run |
| [BLDR-010](BLDR-010.md) | P1 | 6 | todo | Module definition inside the new app (one or more modules, icons, colors) |
| [BLDR-011](BLDR-011.md) | P1 | 6 | todo | Git initialization with branch name, `.gitignore` and first commit |
| [BLDR-012](BLDR-012.md) | P1 | 6 | todo | Pre-commit config, linters and formatter config generation |
| [BLDR-013](BLDR-013.md) | P1 | 6 | todo | README, LICENSE, CHANGELOG and CONTRIBUTING generation |
| [BLDR-014](BLDR-014.md) | P1 | 6 | todo | CI workflow scaffold (lint, unit tests, install-on-bench test) for v15 and v16 |
| [BLDR-015](BLDR-015.md) | P1 | 6 | todo | Test scaffold with a passing smoke test and a permissions test template |
| [BLDR-016](BLDR-016.md) | P1 | 6 | todo | Frontend scaffold option (Vite + Vue + Frappe UI) for apps that need an SPA |
| [BLDR-017](BLDR-017.md) | P1 | 6 | todo | Docker/devcontainer files option for reproducible development |
| [BLDR-018](BLDR-018.md) | P2 | 11 | todo | Scaffold presets: "customizations only", "custom doctypes", "integration app", "reporting app", "SPA app" |
| [BLDR-019](BLDR-019.md) | P2 | 11 | todo | Organization template repository support (your company's own scaffold with standards baked in) |
| [BLDR-020](BLDR-020.md) | P2 | 11 | todo | Brand and header injection (copyright header, publisher info) from THEM brand kit |

## Customization export

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [BLDR-021](BLDR-021.md) | P0 | 6 | todo | Export selector listing all exportable items (Custom Field, Property Setter, Custom DocPerm, Client/Server Script, Print Format, Workflow, Notification, Report, Workspace, Dashboard Chart, Number Card, Email Template, Letterhead, Role, Role Profile, Module Onboarding, Web Form, Translation, Webhook, Assignment Rule, Auto Repeat) |
| [BLDR-022](BLDR-022.md) | P0 | 6 | todo | Target app picker (existing custom app or newly generated one) with writability check |
| [BLDR-023](BLDR-023.md) | P0 | 6 | todo | Fixtures export with per-doctype filters that are written into `hooks.py` safely |
| [BLDR-024](BLDR-024.md) | P0 | 6 | todo | Safe `hooks.py` editor (AST-based merge, never string-splice; preserves comments and formatting where possible) |
| [BLDR-025](BLDR-025.md) | P0 | 6 | todo | Diff preview of every file to be added or changed in the target app |
| [BLDR-026](BLDR-026.md) | P0 | 6 | todo | Idempotent re-export (running twice produces no diff) |
| [BLDR-027](BLDR-027.md) | P0 | 6 | todo | Dependency detection (custom field needs its doctype's app, workflow needs roles and states) |
| [BLDR-028](BLDR-028.md) | P0 | 6 | todo | Automatic inclusion of required dependencies with explanation |
| [BLDR-029](BLDR-029.md) | P0 | 6 | todo | Conflict detection against files already in the target app |
| [BLDR-030](BLDR-030.md) | P1 | 6 | todo | Export custom DocTypes to module folders as standard doctype JSON with controller stubs |
| [BLDR-031](BLDR-031.md) | P1 | 6 | todo | Export Print Formats to standard files (HTML/JSON) in module folders |
| [BLDR-032](BLDR-032.md) | P1 | 6 | todo | Export Reports (query and script) into standard report folders with filters and roles |
| [BLDR-033](BLDR-033.md) | P1 | 6 | todo | Export Workspaces, Dashboard Charts and Number Cards into the module |
| [BLDR-034](BLDR-034.md) | P1 | 6 | todo | Export Client Scripts to JS files and wire them via `doctype_js` hooks, with review gate |
| [BLDR-035](BLDR-035.md) | P1 | 6 | todo | Export Server Scripts to reviewed Python modules and wire them via `doc_events`/API, never auto-run unreviewed code |
| [BLDR-036](BLDR-036.md) | P1 | 6 | todo | Export permissions (Custom DocPerm and ladder matrix from PERM) as fixtures or as an install patch |
| [BLDR-037](BLDR-037.md) | P1 | 6 | todo | Export role profiles, roles and workflow definitions with dependency ordering |
| [BLDR-038](BLDR-038.md) | P1 | 6 | todo | Export translations (scoped ones from TRNS) into the app's translations folder |
| [BLDR-039](BLDR-039.md) | P1 | 6 | todo | Export theme tokens and custom CSS as app assets (after the CSS-injection scan) |
| [BLDR-040](BLDR-040.md) | P1 | 6 | todo | Export onboarding flows and custom HTML blocks |
| [BLDR-041](BLDR-041.md) | P1 | 6 | todo | Export Enhanced View definitions (VIEW) and Automation rules (AUTO) as fixtures |
| [BLDR-042](BLDR-042.md) | P1 | 6 | todo | Export seeder recipes and scenario packs (DATA) as demo-data fixtures |
| [BLDR-043](BLDR-043.md) | P1 | 6 | todo | Patch generator: record data changes as an idempotent patch with `patches.txt` registration |
| [BLDR-044](BLDR-044.md) | P1 | 6 | todo | Move a customization: export then remove from the site's database layer (opt-in, with snapshot) |
| [BLDR-045](BLDR-045.md) | P1 | 6 | todo | Selection by tag, module, doctype, owner, modified-since, or saved selection set |
| [BLDR-046](BLDR-046.md) | P1 | 6 | todo | Sensitive-data scan before export (secrets in scripts, emails, API keys, passwords in fixtures) |
| [BLDR-047](BLDR-047.md) | P1 | 6 | todo | Exclusion rules (never export system-managed or site-specific records) |
| [BLDR-048](BLDR-048.md) | P1 | 6 | todo | Export summary report with counts, warnings and skipped items |
| [BLDR-049](BLDR-049.md) | P2 | 11 | todo | Export profiles saved per app (repeatable "export everything for Sales customizations") |
| [BLDR-050](BLDR-050.md) | P2 | 11 | todo | Scheduled export that opens a draft change set for review rather than writing directly |

## Sync, drift and lifecycle

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [BLDR-051](BLDR-051.md) | P1 | 6 | todo | Drift detector between site customizations and the app's exported files |
| [BLDR-052](BLDR-052.md) | P1 | 6 | todo | "Pull" direction: import app files back to the site with preview |
| [BLDR-053](BLDR-053.md) | P1 | 6 | todo | Install-app flow on a chosen site with pre-checks, backup, and rollback plan |
| [BLDR-054](BLDR-054.md) | P1 | 6 | todo | Uninstall-app flow with orphan check, data impact preview and mandatory backup |
| [BLDR-055](BLDR-055.md) | P1 | 6 | todo | Version bump and changelog entry generation from detected changes |
| [BLDR-056](BLDR-056.md) | P1 | 6 | todo | App health check (hooks valid, imports resolve, fixtures load, patches run) in a temporary site or dry-run |
| [BLDR-057](BLDR-057.md) | P1 | 6 | todo | Migration safety review (patch ordering, destructive operations flagged) |
| [BLDR-058](BLDR-058.md) | P1 | 6 | todo | Generate unit and permission tests for exported customizations (links to TSTD) |
| [BLDR-059](BLDR-059.md) | P2 | 11 | todo | Git integration: commit, branch, tag, push to configured remote with token stored securely |
| [BLDR-060](BLDR-060.md) | P2 | 11 | todo | Pull-request creation with auto-generated description of exported changes |
| [BLDR-061](BLDR-061.md) | P2 | 11 | todo | Release packaging as archive with checksum and signature |
| [BLDR-062](BLDR-062.md) | P2 | 11 | todo | App bundle import on another site (offline transfer of an exported app) |
| [BLDR-063](BLDR-063.md) | P2 | 11 | todo | Multi-app workspace: split customizations across several apps by module or ownership |
| [BLDR-064](BLDR-064.md) | P2 | 11 | todo | Move items between custom apps with reference updates |
| [BLDR-065](BLDR-065.md) | P2 | 11 | todo | Fork/clone an existing custom app under a new name |
| [BLDR-066](BLDR-066.md) | P2 | 11 | todo | Compatibility matrix per app (tested on v15, v16) with badges |
| [BLDR-067](BLDR-067.md) | P2 | 11 | todo | App dependency graph visualization |
| [BLDR-068](BLDR-068.md) | P2 | 11 | todo | App inventory with owner, purpose, last export, last release, health |
| [BLDR-069](BLDR-069.md) | P2 | 11 | todo | Deprecation helper (mark app items obsolete, generate removal patches) |
| [BLDR-070](BLDR-070.md) | P2 | 11 | todo | Customization-to-code explainer (shows which UI customization became which file) |
