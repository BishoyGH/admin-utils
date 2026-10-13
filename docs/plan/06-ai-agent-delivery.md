## 6. AI-Agent Delivery Model

This app is built primarily by AI agents under human supervision. The catalogue is deliberately large so that agents always have well-scoped work; the process below keeps that work consistent and safe.

### 6.1 Work units
- **Feature spec** (one per feature ID): goal, user story, acceptance criteria (Given/When/Then), API contract (inputs, outputs, errors), permissions required, audit events emitted, i18n keys, test list, and risks.
- **Work package** = 3 to 10 related features from one module, small enough to review in one sitting.
- **Contract first:** API schemas, doctype JSON and Vue prop contracts are written and reviewed before implementation; implementation agents cannot change a contract without a contract-change request.

### 6.2 Agent roles
| Role | Responsibility |
|---|---|
| Architect | module boundaries, contracts, ADRs, compat-layer design |
| Implementer (backend) | services, API endpoints, doctypes, patches |
| Implementer (frontend) | Vue pages, components, composables, i18n, RTL |
| Test author | unit, integration, functional, e2e, visual tests from the spec's test list |
| Security reviewer | authz matrix, injection review, secrets handling, privileged-feature review |
| Compatibility agent | v15/v16 differences, CI matrix failures, upgrade tests |
| UX/accessibility reviewer | keyboard, ARIA, contrast, Arabic/RTL screenshots |
| Docs agent | docs pages, changelog, in-app help (KNOW) |
| Release agent | versioning, packaging, release notes |

### 6.3 Rules for agents
1. Work only inside the assigned module directory; cross-module changes go through published interfaces.
2. Every commit, test and PR references feature IDs (e.g. `PERM-016`) for traceability.
3. No feature is "done" until its spec's tests exist, pass on v15 and v16, and the security reviewer role has signed off where the feature is privileged.
4. Agents never receive production credentials or real customer data; they work on disposable benches with seeded data (DATA).
5. Privileged modules (BNCH, CONF, F2B, BLDR, MIGR, SECU, BKUP, AIAS) require a human approval gate on the design and on the merge.
6. Generated code is formatted, linted, type-checked and scanned before it opens a PR.
7. Agents record decisions as ADRs and keep an up-to-date `AGENTS.md` per module (conventions, commands, pitfalls).

### 6.4 Quality loop
- **Definition of Ready:** spec complete, contract reviewed, dependencies available, test list agreed.
- **Per-PR automation:** lint, types, unit, integration, security scan, contract tests, a11y checks, screenshot diffs (LTR and RTL).
- **Nightly:** full matrix on v15, v16 and `develop`; mutation tests on permission and export logic; dependency updates.
- **Weekly human review:** a sample of merged work, flaky tests, security findings, spec drift.
- **Metrics:** features completed per wave, escaped defects, review rework rate, test flake rate, time to green.
