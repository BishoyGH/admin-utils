# AGENTS.md — admin_utils

Standalone Frappe management app (working name `admin_utils`): permissions ladder manager, report designer, bench-from-UI, theme/onboarding/training, monitoring, logs, and more. Targets Frappe **v15 and v16**. Frontend: **Vue 3 + frappe-ui + Tailwind** SPA at `/manage`, reachable from the app switcher. It **never overrides core Frappe**; it extends only through documented hooks. New views (e.g. enhanced Kanban) are additive.

1815 features, each one a task file. You are expected to work on **one task at a time**.

## Where things are

| Path | What |
|---|---|
| `docs/tasks/<CODE>/<ID>.md` | One task per feature (front matter = status, priority, wave, deps) |
| `docs/specs/NN-<module>.md` | Module spec: scope, groups, tests, risks, decisions |
| `docs/contracts/` | API/doctype/prop contracts (written before code) |
| `docs/adr/` | Architecture decision records |
| `docs/waves/` | Delivery order and exit criteria |
| `docs/agents/<role>.md` | Role instructions |
| `docs/checklists/` | Definition of Ready / Done, privileged review |
| `docs/plan/` | Vision, architecture, best practices, test strategy, roadmap, risks |
| `admin_utils/<package>/AGENTS.md` | Module conventions (keep current) |
| `scripts/tasks.py` | Task CLI |

## Task protocol

1. `python scripts/tasks.py next` (or `list --module X --wave N`) then `show ID`.
2. Read the task, its module spec and module `AGENTS.md`, and any referenced tasks.
3. **Definition of Ready** (`docs/checklists/definition-of-ready.md`): write the acceptance criteria (Given/When/Then) in the task, and get the contract written/approved in `docs/contracts/`. Set status `ready`.
4. `set-status ID in-progress`, implement, write tests from the task's list, update docs and i18n.
5. Open a PR titled `ID: short summary` (e.g. `PERM-016: block delete of cancelled docs`). Every commit and test references the ID. Status `in-review`.
6. Meet the **Definition of Done** (`docs/checklists/definition-of-done.md`), then `set-status ID done`. Record decisions as ADRs and note PR links in the task.
7. Blocked? set `blocked` and write why in the task Notes. Do not invent scope; do not work on a task whose referenced tasks are not done.

## Golden rules

- **Layering:** `api/` (thin: auth + validation) -> `services/` (logic, no `frappe.whitelist`) -> `core/compat` (all v15/v16 differences) -> Frappe. The UI talks only to `api/`.
- **Every endpoint** goes through the central `guard()` (role + feature flag + rate limit) and returns the standard envelope `{ok, data, error, trace_id}`.
- **Every mutating action** writes an immutable audit row (who, what, when, IP, before/after).
- **Bulk or risky changes:** preview/diff first, snapshot before apply, one-click rollback, dry-run where possible.
- **No shell, ever.** No `shell=True`, no string-built commands, no raw SQL from user input (parameterized only, SELECT-only where user-defined). Process execution uses allowlisted argv lists.
- **Secrets:** never in logs, UI, exports or errors; use the central masking utility on read paths.
- **i18n + RTL:** every user-facing string translatable (EN + AR shipped); logical CSS properties; test LTR and RTL.
- **Feature flags:** each module has `enable_<package>` in `Admin Utils Settings`; privileged modules are off by default.
- **Module boundaries:** work inside the task's module directories; cross-module changes go through published service interfaces or a contract-change request.
- **Contracts first:** do not change an approved contract without a contract-change request (`docs/contracts/README.md`).
- **Tests:** a task is not done without tests that pass on v15 and v16. Never weaken or delete a test to get green.
- **Safety:** you never receive or use production credentials or real customer data; use disposable benches with seeded data. Do not install apps or run destructive commands outside the sandbox bench.

## Privileged modules

`BNCH, CONF, F2B, SECU, BLDR, MIGR, BKUP, AIAS` need a **human approval gate on the design and on the merge**, two reviewers, and security-reviewer sign-off (`docs/checklists/privileged-review.md`). Do not merge them on your own.

## Commands (adapt to your bench; keep this section current)

```
python scripts/tasks.py stats                 # progress overview
python scripts/tasks.py next --role backend   # next ready-to-pick task
bench --site <test_site> run-tests --app admin_utils --module admin_utils.<package>.tests
cd frontend && yarn test && yarn lint && yarn type-check
```

## Commit / PR conventions

`<TASK-ID>: imperative summary`. One task per PR where possible (work package = 3 to 10 related tasks from one module at most). PR template in `.github/pull_request_template.md`.

## Roles

architect, implementer-backend, implementer-frontend, test-author, security-reviewer, compatibility, ux-a11y, docs, release — see `docs/agents/`.
