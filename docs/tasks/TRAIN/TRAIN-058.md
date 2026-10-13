---
id: TRAIN-058
title: "Content review cycle with owners and expiry dates"
module: TRAIN
group: "Trainer & admin tools"
priority: P2
wave: 11
status: todo
privileged: false
masking_required: false
module_depends_on: [CORE, ONBD, GUID, DATA, PERM, GOVN]
references: []
spec: docs/specs/34-training-academy.md
code_path: admin_utils/training/
roles: [implementer-backend, implementer-frontend, test-author]
---

# TRAIN-058 — Content review cycle with owners and expiry dates

**Module:** Training Academy (`TRAIN`) · **Group:** Trainer & admin tools · **Priority:** P2 · **Wave:** 11 · **Status:** see front matter

## Goal

Content review cycle with owners and expiry dates

## Read first

1. `AGENTS.md` (rules for every agent)
2. [`34-training-academy.md`](../../specs/34-training-academy.md) — module spec (scope, groups, tests, risks)
3. `admin_utils/training/AGENTS.md` — module conventions
4. Module prerequisites: `CORE`, `ONBD`, `GUID`, `DATA`, `PERM`, `GOVN` (see spec)

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
- [ ] Module-specific test requirements in the spec (section *Tests*): [`34-training-academy.md`](../../specs/34-training-academy.md)

## Definition of done

- [ ] Spec/contract merged before code · [ ] LTR + RTL screenshots and a11y check (if UI)
- [ ] Audit entries for every mutating action · [ ] Behind a feature flag, default documented
- [ ] Docs + EN/AR strings updated · [ ] Lint, types, scans clean · [ ] CI green on v15 and v16
- [ ] Review by one other reviewer

## Notes / PR links

_Agents: append dated notes, decisions (link ADRs) and PR links here. Commit and PR titles must start with the task ID._
