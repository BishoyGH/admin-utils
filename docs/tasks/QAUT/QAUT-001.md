---
id: QAUT-001
title: "In-app \"Self-test\" page running safe diagnostics for every enabled module"
module: QAUT
group: "Core"
priority: P0
wave: 0
status: todo
privileged: false
masking_required: false
module_depends_on: [CORE]
references: []
spec: docs/specs/23-self-test.md
code_path: admin_utils/selftest/
roles: [implementer-backend, implementer-frontend, test-author]
---

# QAUT-001 — In-app "Self-test" page running safe diagnostics for every enabled module

**Module:** Built-in Self-Test & Diagnostics (`QAUT`) · **Group:** Core · **Priority:** P0 · **Wave:** 0 · **Status:** see front matter

## Goal

In-app "Self-test" page running safe diagnostics for every enabled module

## Read first

1. `AGENTS.md` (rules for every agent)
2. [`23-self-test.md`](../../specs/23-self-test.md) — module spec (scope, groups, tests, risks)
3. `admin_utils/selftest/AGENTS.md` — module conventions
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
- [ ] Module-specific test requirements in the spec (section *Tests*): [`23-self-test.md`](../../specs/23-self-test.md)

## Definition of done

- [ ] Spec/contract merged before code · [ ] LTR + RTL screenshots and a11y check (if UI)
- [ ] Audit entries for every mutating action · [ ] Behind a feature flag, default documented
- [ ] Docs + EN/AR strings updated · [ ] Lint, types, scans clean · [ ] CI green on v15 and v16
- [ ] Review by one other reviewer

## Notes / PR links

_Agents: append dated notes, decisions (link ADRs) and PR links here. Commit and PR titles must start with the task ID._
