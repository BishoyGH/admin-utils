---
id: SECU-014
title: "HTTPS/HSTS and certificate checks"
module: SECU
group: "Core"
priority: P1
wave: 4
status: todo
privileged: true
masking_required: false
module_depends_on: [CORE]
references: []
spec: docs/specs/14-security-center.md
code_path: admin_utils/security/
roles: [implementer-backend, implementer-frontend, test-author, security-reviewer]
---

# SECU-014 — HTTPS/HSTS and certificate checks

**Module:** Security Center (`SECU`) · **Group:** Core · **Priority:** P1 · **Wave:** 4 · **Status:** see front matter

## Goal

HTTPS/HSTS and certificate checks

## Read first

1. `AGENTS.md` (rules for every agent)
2. [`14-security-center.md`](../../specs/14-security-center.md) — module spec (scope, groups, tests, risks)
3. `admin_utils/security/AGENTS.md` — module conventions
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
- [ ] Security review sign-off recorded in Notes (privileged module)
- [ ] Module-specific test requirements in the spec (section *Tests*): [`14-security-center.md`](../../specs/14-security-center.md)

## Definition of done

- [ ] Spec/contract merged before code · [ ] LTR + RTL screenshots and a11y check (if UI)
- [ ] Audit entries for every mutating action · [ ] Behind a feature flag, default documented
- [ ] Docs + EN/AR strings updated · [ ] Lint, types, scans clean · [ ] CI green on v15 and v16
- [ ] Review by two reviewers + human approval gate on design and merge

## Notes / PR links

_Agents: append dated notes, decisions (link ADRs) and PR links here. Commit and PR titles must start with the task ID._
