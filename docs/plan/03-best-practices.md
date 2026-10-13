## 3. Best Practices (mandatory)

### 3.1 Backend
- Whitelist only in `api/`; every endpoint calls a `guard(role, feature)` first; use `methods=["POST"]` for anything mutating.
- Validate inputs with typed schemas (pydantic or `frappe.utils` + custom validators); reject unknown keys.
- Use `frappe.db.sql` only with parameters; prefer `frappe.qb`.
- Use `frappe.enqueue` (queue `long`) for slow work; return a job id and stream progress via `frappe.publish_realtime`.
- Idempotent operations: every apply-step is safe to re-run.
- Wrap multi-step changes in a transaction or a compensating undo snapshot.
- No `ignore_permissions=True` unless inside a guarded service with a comment explaining why.
- Never log secrets; mask `db_password`, `encryption_key`, API secrets everywhere.
- Type hints + `ruff` + `mypy` (strict on `services/` and `core/`).
- Frappe `hooks.py` only: `doc_events`, `permission_query_conditions`, `has_permission`, `scheduler_events`, `add_to_apps_screen`, `after_install`, `after_migrate`.

### 3.2 Frontend
- Vue 3 `<script setup>` + TypeScript; Composition API; Pinia only where shared state is needed (prefer `frappe-ui` resources).
- Lazy-loaded route per feature; code-split heavy editors (Monaco, chart libs).
- Accessibility: WCAG 2.1 AA, keyboard-complete, visible focus, ARIA on custom widgets.
- RTL via logical CSS properties (`ms-*`, `me-*`, `ps-*`); test Arabic layout in CI screenshots.
- All strings via i18n (`__()` equivalent) — zero hardcoded text.
- Design tokens only (no raw hex) so the brand/theme can change in one place.
- Optimistic UI only for safe, reversible actions.

### 3.3 Security
- Dedicated roles: `Admin Utils Manager`, plus sub-roles per risky feature (`Admin Utils Bench Operator`, `Admin Utils Config Editor`, `Admin Utils Security Admin`).
- Allowlist > denylist for shell commands and config keys.
- No shell string interpolation; `subprocess.run([...], shell=False)` with fixed argv templates.
- Rate-limit mutating endpoints; CSRF handled by Frappe; confirm destructive actions with typed confirmation.
- Immutable audit log for every privileged action (who/what/when/IP/before/after).
- Secrets masked in UI, logs, exports and error traces.
- Dependency scanning (`pip-audit`, `npm audit`), SAST (`bandit`, `semgrep`), secret scanning (`gitleaks`).

### 3.4 Quality & Process
- Trunk-based dev, short-lived branches, Conventional Commits, semantic versioning, changelog automation.
- Pre-commit: `ruff`, `black`/`ruff format`, `eslint`, `prettier`, `vue-tsc`, `gitleaks`.
- PR template with test evidence, security checklist, screenshot (LTR + RTL).
- ADRs (`docs/adr/`) for every non-trivial decision.
- Feature flags for anything unfinished; no long-lived branches.
- Definition of Done in 10-definition-of-done.md.

### 3.5 Performance
- Server-side pagination/virtualization for any list > 100 rows.
- Cache read-heavy metadata (`frappe.cache`) with explicit invalidation.
- Budgets: SPA initial JS ≤ 250 KB gz; route chunk ≤ 150 KB gz; API p95 ≤ 300 ms (non-job).

### 3.6 Version Compatibility
- `core/compat.py` exposes stable functions (`get_desk_icons()`, `get_workspace_schema()`, `app_switcher_register()`), each with v15/v16 implementations.
- CI matrix runs the full suite on `version-15` and `version-16` (and `develop` nightly).
- Contract tests pin the shape of any core doctype the app writes to.

### 3.7 Observability
- Structured logging via a dedicated logger (`admin_utils`), correlation id per request/job.
- Error → `Error Log` with feature tag; optional Sentry hook.
- Health endpoint for the app itself.
- Log viewing, export, replay and reveal-unmasked actions are role-gated and audited; logs are masked at read time and file access is allowlist-only.
