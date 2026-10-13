# TSTD — Testing Studio: tasks

Spec: [`29-testing-studio.md`](../../specs/29-testing-studio.md) · 25 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [TSTD-001](TSTD-001.md) | P0 | 6 | todo | Test registry listing generated and hand-written tests per app and module |
| [TSTD-002](TSTD-002.md) | P0 | 2 | todo | Run backend tests from the UI as background jobs with live output (test sites only) |
| [TSTD-003](TSTD-003.md) | P0 | 2 | todo | Hard block on running destructive tests against production-flagged environments |
| [TSTD-004](TSTD-004.md) | P1 | 6 | todo | Generate permission tests from the PERM ladder matrix |
| [TSTD-005](TSTD-005.md) | P1 | 6 | todo | Generate workflow tests from workflow definitions (every transition, allowed and denied) |
| [TSTD-006](TSTD-006.md) | P1 | 6 | todo | Generate validation tests from mandatory, unique and link rules per doctype |
| [TSTD-007](TSTD-007.md) | P1 | 6 | todo | Generate report tests (runs without error, totals reconcile against fixtures) |
| [TSTD-008](TSTD-008.md) | P1 | 6 | todo | Generate print format render tests (renders, page count, no template errors) |
| [TSTD-009](TSTD-009.md) | P1 | 6 | todo | Generate notification and automation rule tests with simulated events |
| [TSTD-010](TSTD-010.md) | P1 | 2 | todo | Test data builders backed by the DATA seeder (deterministic) |
| [TSTD-011](TSTD-011.md) | P1 | 2 | todo | Test results history with trends, flaky-test detection and failure grouping |
| [TSTD-012](TSTD-012.md) | P1 | 6 | todo | Export generated tests into a target custom app (via BLDR) in the right folders |
| [TSTD-013](TSTD-013.md) | P1 | 2 | todo | Customization coverage view (which customizations have tests) |
| [TSTD-014](TSTD-014.md) | P1 | 2 | todo | Pre-promotion test gate in MIGR (block if tests fail) |
| [TSTD-015](TSTD-015.md) | P2 | 11 | todo | E2E flow recorder that produces Playwright specs for common admin journeys |
| [TSTD-016](TSTD-016.md) | P2 | 11 | todo | Visual snapshot management (approve, reject, diff) for pages and print formats |
| [TSTD-017](TSTD-017.md) | P2 | 11 | todo | Accessibility test runner against key pages |
| [TSTD-018](TSTD-018.md) | P2 | 11 | todo | Security test pack runner (authz matrix, injection payloads on custom endpoints) |
| [TSTD-019](TSTD-019.md) | P2 | 6 | todo | Load test scenario generator from seeded data profiles |
| [TSTD-020](TSTD-020.md) | P2 | 11 | todo | Mutation-style checks for permission rules (flip a flag, tests must fail) |
| [TSTD-021](TSTD-021.md) | P2 | 11 | todo | Test environment provisioner (clone and seed a throwaway site) |
| [TSTD-022](TSTD-022.md) | P2 | 11 | todo | Scheduled regression runs with NTFY alerts |
| [TSTD-023](TSTD-023.md) | P2 | 11 | todo | Test impact analysis (which tests to run for a given change set) |
| [TSTD-024](TSTD-024.md) | P2 | 6 | todo | Test documentation generator (what is covered, what is not) |
| [TSTD-025](TSTD-025.md) | P2 | 11 | todo | Export results as JUnit/HTML for external CI |
