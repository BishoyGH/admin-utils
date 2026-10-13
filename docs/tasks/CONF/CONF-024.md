---
id: CONF-024
title: "Show effective config (site + common + environment overrides)"
module: CONF
group: "Core"
priority: P2
wave: 11
status: todo
privileged: true
masking_required: true
module_depends_on: [CORE]
references: []
spec: docs/specs/04-site-config.md
code_path: admin_utils/siteconfig/
roles: [implementer-backend, implementer-frontend, test-author, security-reviewer]
---

# CONF-024 — Show effective config (site + common + environment overrides)

**Module:** Site Config JSON Editor (`CONF`) · **Group:** Core · **Priority:** P2 · **Wave:** 11 · **Status:** see front matter

## Goal

Show effective config (site + common + environment overrides)

## Read first

1. `AGENTS.md` (rules for every agent)
2. [`04-site-config.md`](../../specs/04-site-config.md) — module spec (scope, groups, tests, risks)
3. `admin_utils/siteconfig/AGENTS.md` — module conventions
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
- [ ] Masking test: planted secrets/personal data never reach UI, export, or alert
- [ ] Security review sign-off recorded in Notes (privileged module)
- [ ] Module-specific test requirements in the spec (section *Tests*): [`04-site-config.md`](../../specs/04-site-config.md)

## Definition of done

- [ ] Spec/contract merged before code · [ ] LTR + RTL screenshots and a11y check (if UI)
- [ ] Audit entries for every mutating action · [ ] Behind a feature flag, default documented
- [ ] Docs + EN/AR strings updated · [ ] Lint, types, scans clean · [ ] CI green on v15 and v16
- [ ] Review by two reviewers + human approval gate on design and merge

## Notes / PR links

_Agents: append dated notes, decisions (link ADRs) and PR links here. Commit and PR titles must start with the task ID._
