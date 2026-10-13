---
id: BNCH-033
title: "Custom command registration API for other apps (still allowlisted)"
module: BNCH
group: "Core"
priority: P2
wave: 4
status: todo
privileged: true
masking_required: false
module_depends_on: [CORE]
references: []
spec: docs/specs/03-bench-commands.md
code_path: admin_utils/bench/
roles: [implementer-backend, implementer-frontend, test-author, security-reviewer]
---

# BNCH-033 — Custom command registration API for other apps (still allowlisted)

**Module:** Run Bench Commands From UI (`BNCH`) · **Group:** Core · **Priority:** P2 · **Wave:** 4 · **Status:** see front matter

## Goal

Custom command registration API for other apps (still allowlisted)

## Read first

1. `AGENTS.md` (rules for every agent)
2. [`03-bench-commands.md`](../../specs/03-bench-commands.md) — module spec (scope, groups, tests, risks)
3. `admin_utils/bench/AGENTS.md` — module conventions
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

## Tests required

- [ ] Backend unit + integration; frontend unit/component where UI exists
- [ ] Authorization test: denied for roles without access (security matrix in `docs/plan/05-testing-strategy.md`)
- [ ] Security review sign-off recorded in Notes (privileged module)
- [ ] Module-specific test requirements in the spec (section *Tests*): [`03-bench-commands.md`](../../specs/03-bench-commands.md)

## Definition of done

- [ ] Spec/contract merged before code · [ ] LTR + RTL screenshots and a11y check (if UI)
- [ ] Audit entries for every mutating action · [ ] Behind a feature flag, default documented
- [ ] Docs + EN/AR strings updated · [ ] Lint, types, scans clean · [ ] CI green on v15 and v16
- [ ] Review by two reviewers + human approval gate on design and merge

## Notes / PR links

_Agents: append dated notes, decisions (link ADRs) and PR links here. Commit and PR titles must start with the task ID._
