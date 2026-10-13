---
id: THEM-094
title: "Email header, footer and button styling synced from the theme"
module: THEM
group: "Brand & delivery"
priority: P1
wave: 3
status: todo
privileged: false
masking_required: false
module_depends_on: [CORE]
references: []
spec: docs/specs/06-theme-studio.md
code_path: admin_utils/theme/
roles: [implementer-backend, implementer-frontend, test-author]
---

# THEM-094 — Email header, footer and button styling synced from the theme

**Module:** Theme Studio (`THEM`) · **Group:** Brand & delivery · **Priority:** P1 · **Wave:** 3 · **Status:** see front matter

## Goal

Email header, footer and button styling synced from the theme

## Read first

1. `AGENTS.md` (rules for every agent)
2. [`06-theme-studio.md`](../../specs/06-theme-studio.md) — module spec (scope, groups, tests, risks)
3. `admin_utils/theme/AGENTS.md` — module conventions
4. Module prerequisites: `CORE` (see spec)

## Contract (write and review before implementing)

- [ ] API: endpoint name, inputs, outputs, error codes (standard envelope `ok/data/error/trace_id`)
- [ ] Doctypes / fields / patches touched
- [ ] Permissions and feature flag required
- [ ] Audit events emitted (mutating actions)
- [ ] i18n keys (EN + AR)

## Acceptance criteria

- [ ] Given / When / Then written by the spec agent (replace this line; at least one happy path and one denied/invalid path)
- [ ] Behaviour matches the goal above, on Frappe v15 and v16
- [ ] Primary user journey covered by an e2e test

## Tests required

- [ ] Backend unit + integration; frontend unit/component where UI exists
- [ ] Authorization test: denied for roles without access (security matrix in `docs/plan/05-testing-strategy.md`)
- [ ] Module-specific test requirements in the spec (section *Tests*): [`06-theme-studio.md`](../../specs/06-theme-studio.md)

## Definition of done

- [ ] Spec/contract merged before code · [ ] LTR + RTL screenshots and a11y check (if UI)
- [ ] Audit entries for every mutating action · [ ] Behind a feature flag, default documented
- [ ] Docs + EN/AR strings updated · [ ] Lint, types, scans clean · [ ] CI green on v15 and v16
- [ ] Review by one other reviewer

## Notes / PR links

_Agents: append dated notes, decisions (link ADRs) and PR links here. Commit and PR titles must start with the task ID._
