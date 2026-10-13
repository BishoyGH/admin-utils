---
id: CORE-031
title: "Toast/notification system integrated with job results"
module: CORE
group: "Core"
priority: P1
wave: 0
status: todo
privileged: false
masking_required: false
module_depends_on: []
references: []
spec: docs/specs/00-core-platform.md
code_path: admin_utils/core/
roles: [implementer-backend, implementer-frontend, test-author]
---

# CORE-031 — Toast/notification system integrated with job results

**Module:** Platform, Shell & Cross-Cutting (`CORE`) · **Group:** Core · **Priority:** P1 · **Wave:** 0 · **Status:** see front matter

## Goal

Toast/notification system integrated with job results

## Read first

1. `AGENTS.md` (rules for every agent)
2. [`00-core-platform.md`](../../specs/00-core-platform.md) — module spec (scope, groups, tests, risks)
3. `admin_utils/core/AGENTS.md` — module conventions

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
- [ ] Module-specific test requirements in the spec (section *Tests*): [`00-core-platform.md`](../../specs/00-core-platform.md)

## Definition of done

- [ ] Spec/contract merged before code · [ ] LTR + RTL screenshots and a11y check (if UI)
- [ ] Audit entries for every mutating action · [ ] Behind a feature flag, default documented
- [ ] Docs + EN/AR strings updated · [ ] Lint, types, scans clean · [ ] CI green on v15 and v16
- [ ] Review by one other reviewer

## Notes / PR links

_Agents: append dated notes, decisions (link ADRs) and PR links here. Commit and PR titles must start with the task ID._
