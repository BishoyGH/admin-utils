## 5. Testing Strategy

**Principle:** test pyramid with extra weight on security and permissions, because this app manages access, config and shell-adjacent operations.

| Layer | Scope | Tools | Target |
|---|---|---|---|
| Unit (backend) | services, validators, compat layer, guards | `pytest` + `frappe.tests` (`FrappeTestCase`), `hypothesis` for property tests | ≥ 90% line, ≥ 85% branch on `services/` and `core/` |
| Unit (frontend) | composables, stores, utils | `vitest` | ≥ 85% |
| Component | Vue components in isolation (a11y included) | `vitest` + Vue Test Utils, `@testing-library/vue`, `axe-core` | every shared component |
| Integration | API endpoints against a real site/DB | `bench run-tests`, `pytest` | every whitelisted endpoint |
| Functional | feature flows end to end on the backend (e.g. apply ladder → verify effective perms) | `FrappeTestCase` scenarios | every P0/P1 feature |
| E2E | real browser against a seeded site | `Playwright` (Chromium, Firefox, WebKit) | every critical user journey |
| UI / visual | screenshot regression (LTR + RTL, light + dark, 3 viewports) | Playwright snapshots / Percy-style diff | every page |
| Accessibility | WCAG 2.1 AA | `axe-core` in Playwright, manual keyboard audit | zero serious/critical violations |
| Security | authz, injection, secrets, CSRF, rate limits | see 05-testing-strategy.md §5.1 | zero high/critical findings |
| Performance | API latency, big lists, seeding, bundle size | `locust`/`k6`, Lighthouse CI, `size-limit` | budgets in 03-best-practices.md §3.5 |
| Compatibility | v15 × v16 (× `develop` nightly) | CI matrix | all suites green on both |
| Migration/upgrade | install, upgrade from N-1, uninstall | scripted bench scenarios | clean, idempotent |
| Resilience | job failure, crash mid-apply, partial rollback | fault-injection tests | rollback always restores state |
| i18n/RTL | Arabic strings, RTL layout, mixed text | Playwright + string-lint | zero missing keys |
| Contract | shape of core doctypes the app writes to | schema snapshot tests | fail on drift |
| Mutation (optional) | test effectiveness | `mutmut` on `services/permissions` | ≥ 70% killed |

### 5.1 Security Test Matrix

- **AuthZ:** for every endpoint, test as Guest, plain user, wrong-sub-role admin, and correct role. Only the last succeeds.
- **Feature flags:** disabled feature → endpoint returns 403/404 even for System Manager.
- **Injection:** SQLi payloads in report designer, filters, seeder expressions; command-injection payloads in bench args; path traversal in file/log viewers and config editor.
- **Allowlists:** attempt unlisted bench commands, forbidden config keys, unlisted jails, non-IP strings for ban/unban.
- **Generated code:** scaffolded apps and exported scripts are scanned with bandit/semgrep inside the generator's own tests; template-injection tests prove user input cannot become executable code.
- **XSS/CSS injection:** workspace HTML block, theme custom CSS, translation strings, onboarding rich text, report labels.
- **Secrets:** assert masking in API responses, logs, audit entries, exports and error traces.
- **CSRF/method:** mutating endpoints reject GET and missing tokens.
- **Rate limiting & lockout:** repeated destructive calls throttled.
- **Audit integrity:** every privileged action creates an audit row; audit rows cannot be edited/deleted via API.
- **Self-lockout:** cannot ban own IP, remove own admin role, or lock the config in a way that disables recovery.
- **Static analysis:** `bandit`, `semgrep` (Python + Vue), `eslint-plugin-security`; dependency scans (`pip-audit`, `npm audit`, `osv-scanner`); `gitleaks`.
- **Fuzzing:** schema-based fuzz on all whitelisted endpoints (`schemathesis`-style via generated OpenAPI).
- **Pen-test checklist** before each minor release (OWASP ASVS L2 subset).

### 5.2 Feature-Specific Test Highlights

- **PERM:** golden-file tests of the generated Custom DocPerm set per level; property test that inheritance is monotonic (a higher level never has fewer flags); tests that `junior` cannot submit, `self-support` cannot delete submitted/cancelled, `senior` cannot cancel, only `auditor` can; rollback restores exact prior rows; idempotent re-apply yields no diff.
- **REPT:** generated SQL is parameterized; non-SELECT rejected; row- and column-level security respected; round trip designer → saved report → run.
- **BNCH:** argv construction snapshot tests, timeout/cancel tests, concurrency lock, no shell metacharacter ever reaches a shell; mocked `bench` binary in CI plus one real smoke job.
- **CONF:** atomic write under simulated crash, backup created before write, secret masking, restore works.
- **TRNS:** resolution order matrix, placeholder integrity, cache invalidation.
- **THEM:** token → CSS compile snapshots, contrast checker vectors, CSS-injection blocklist.
- **LOGS/DBUG/TRCE:** parser tests against recorded fixtures for every supported format; multi-line and rotated-file handling; path-traversal and symlink attack tests; masking tests that plant secrets and personal data and assert they never reach the UI, exports or alerts; large-file performance tests; fingerprinting accuracy tests on a corpus of real-looking errors; reproduction-bundle sanitization tests; replay is refused against production-flagged environments; tracing overhead stays within budget under load.
- **WKSP/ONBD:** v15/v16 schema compat fixtures, broken-link detection.
- **DATA:** determinism with fixed seed, dependency ordering, all docstatus variants, batch delete cleans everything, Arabic provider output validation.
- **MNTR/F2B:** collectors tested with recorded fixtures; fail2ban client wrapped behind an interface and tested with a fake binary; real integration test in a container with fail2ban installed.
- **VIEW:** drag-drop e2e, permission-filtered result sets, workflow-blocked moves, virtualization performance test with 10k+ rows.
- **BLDR/MIGR:** generated apps install and pass their own CI on v15 and v16; re-export is idempotent (zero diff); AST-based `hooks.py` edits preserve unrelated content; the sensitive-data scan catches planted secrets; promote then rollback restores the exact prior state.
- **BKUP:** automated restore test to a throwaway site proves every backup type is restorable; retention dry-runs never delete the newest valid backup.
- **AIAS:** golden-prompt evaluation harness; data-minimization tests prove masked fields never leave the server; generated SQL/code passes static safety filters before preview.
- **ONBD/GUID/TRAIN:** nightly Playwright playback of every flow on v15 and v16 in LTR and RTL; anchor-resilience tests that mutate the DOM; sandbox-isolation tests proving no email, webhook or payment leaves the training environment; task-verification tests with known-good and known-bad end states; keyboard-only and screen-reader walkthroughs; reading-level checks on shipped content.
- **THEM:** contrast auto-repair test vectors; assignment-rule precedence matrix; rollback restores the exact prior tokens; theme package export/import round trip; screenshot baselines per theme in light, dark, LTR and RTL.

### 5.3 Test Data & Environments

- Test site factory (`tests/factories/`) creating roles, users per level, companies, and seeded datasets (uses DATA module in CI).
- Fixtures per scenario: `empty_site`, `retail_small`, `accounting_full`, `multi_company`.
- Ephemeral CI benches (Docker) for v15 and v16; nightly `develop`.
- Playwright auth states per role to avoid repeated logins.
- Deterministic clocks and seeds; no network calls in tests (mock external providers).

### 5.4 CI/CD Pipeline

1. **Pre-commit/lint:** ruff, mypy, eslint, vue-tsc, prettier, gitleaks.
2. **Unit:** backend + frontend in parallel.
3. **Integration/functional:** matrix `[v15, v16] × [MariaDB 10.6/11]`.
4. **Security:** bandit, semgrep, dependency scans, security test suite.
5. **Build:** frontend production build + bundle-size check.
6. **E2E + visual + a11y:** Playwright on seeded site, sharded.
7. **Perf smoke:** k6 baseline + Lighthouse.
8. **Upgrade test:** install previous release → migrate → run smoke suite.
9. **Release:** semantic-release, changelog, signed tag, artifacts.
10. **Nightly:** full suite on `develop`, mutation tests, fuzzing, dependency updates.

**Merge gates:** all required checks green, coverage not decreased, no new high/critical security findings, screenshot diffs reviewed, changelog entry present.
