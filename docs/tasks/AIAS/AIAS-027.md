---
id: AIAS-027
title: "Cost and usage dashboard for assistive calls"
module: AIAS
group: "Core"
priority: P2
wave: 11
status: todo
privileged: true
masking_required: true
module_depends_on: [CORE, GOVN]
references: []
spec: docs/specs/32-assistive-intelligence.md
code_path: admin_utils/assist/
roles: [implementer-backend, implementer-frontend, test-author, security-reviewer]
---

# AIAS-027 — Cost and usage dashboard for assistive calls

**Module:** Assistive Intelligence Layer (`AIAS`) · **Group:** Core · **Priority:** P2 · **Wave:** 11 · **Status:** see front matter

## Goal

Cost and usage dashboard for assistive calls

## Read first

1. `AGENTS.md` (rules for every agent)
2. [`32-assistive-intelligence.md`](../../specs/32-assistive-intelligence.md) — module spec (scope, groups, tests, risks)
3. `admin_utils/assist/AGENTS.md` — module conventions
4. Module prerequisites: `CORE`, `GOVN` (see spec)

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
- [ ] Masking test: planted secrets/personal data never reach UI, export, or alert
- [ ] Security review sign-off recorded in Notes (privileged module)
- [ ] Module-specific test requirements in the spec (section *Tests*): [`32-assistive-intelligence.md`](../../specs/32-assistive-intelligence.md)

## Definition of done

- [ ] Spec/contract merged before code · [ ] LTR + RTL screenshots and a11y check (if UI)
- [ ] Audit entries for every mutating action · [ ] Behind a feature flag, default documented
- [ ] Docs + EN/AR strings updated · [ ] Lint, types, scans clean · [ ] CI green on v15 and v16
- [ ] Review by two reviewers + human approval gate on design and merge

## Notes / PR links

_Agents: append dated notes, decisions (link ADRs) and PR links here. Commit and PR titles must start with the task ID._
