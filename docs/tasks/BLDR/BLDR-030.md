---
id: BLDR-030
title: "Export custom DocTypes to module folders as standard doctype JSON with controller stubs"
module: BLDR
group: "Customization export"
priority: P1
wave: 6
status: todo
privileged: true
masking_required: false
module_depends_on: [CORE, BNCH]
references: []
spec: docs/specs/24-app-builder.md
code_path: admin_utils/builder/
roles: [implementer-backend, implementer-frontend, test-author, security-reviewer]
---

# BLDR-030 — Export custom DocTypes to module folders as standard doctype JSON with controller stubs

**Module:** App Builder & Customization Export (`BLDR`) · **Group:** Customization export · **Priority:** P1 · **Wave:** 6 · **Status:** see front matter

## Goal

Export custom DocTypes to module folders as standard doctype JSON with controller stubs

## Read first

1. `AGENTS.md` (rules for every agent)
2. [`24-app-builder.md`](../../specs/24-app-builder.md) — module spec (scope, groups, tests, risks)
3. `admin_utils/builder/AGENTS.md` — module conventions
4. Module prerequisites: `CORE`, `BNCH` (see spec)

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
- [ ] Module-specific test requirements in the spec (section *Tests*): [`24-app-builder.md`](../../specs/24-app-builder.md)

## Definition of done

- [ ] Spec/contract merged before code · [ ] LTR + RTL screenshots and a11y check (if UI)
- [ ] Audit entries for every mutating action · [ ] Behind a feature flag, default documented
- [ ] Docs + EN/AR strings updated · [ ] Lint, types, scans clean · [ ] CI green on v15 and v16
- [ ] Review by two reviewers + human approval gate on design and merge

## Notes / PR links

_Agents: append dated notes, decisions (link ADRs) and PR links here. Commit and PR titles must start with the task ID._
