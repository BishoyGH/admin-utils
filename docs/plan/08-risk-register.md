## 8. Risk Register

| Risk | Impact | Mitigation |
|---|---|---|
| v15/v16 schema divergence (workspace, desk shell) | High | compat layer, contract tests, nightly `develop` CI |
| Bench/fail2ban misuse or RCE vector | Critical | allowlist, no shell, sub-roles, off by default, pen-test |
| Permission apply breaks live access | High | preview, snapshots, rollback, dry-run, protected roles |
| Frappe UI breaking changes | Medium | pin versions, upgrade in dedicated PRs with visual diffs |
| Scope creep (550+ features) | High | strict P0/P1/P2, phase exits, feature flags |
| Large-data performance in views/reports | Medium | server-side pagination, aggregation endpoints, perf budgets |
| Translation scoping semantic mismatch | Medium | own resolution layer, clear docs, tests |
| Secrets leakage in logs/UI | Critical | central masking, tests, secret scanning |
| Generated apps contain unreviewed or unsafe code | High | fixed templates, human review gate for scripts, sensitive-data scan, sandboxed output directory |
| App creation or installation on production | High | environment policy block, approvals, mandatory backup, canary on a clone |
| AI-agent mistakes in privileged modules | High | contracts first, security-reviewer agent, human gate on privileged P0 work, no production credentials in agent context |
| Agent context drift across a very large catalogue | Medium | per-module spec packs, feature-ID traceability, contract tests |
| Assistive layer leaking data to providers | High | data minimization, masking, allowlisted endpoints, opt-in per feature |
| Guided flows break when the UI changes | Medium | resilient anchors, anchor health dashboard, nightly flow playback, post-upgrade impact list |
| Training sandbox causes real-world side effects (email, webhooks, payments) | High | dedicated company or site, outbound blocking, isolation tests |
| Training content goes stale | Medium | owners, review dates, release-based "what changed" flows |
| Logs and traces expose secrets or personal data | High | read-time masking, role gates per source group, audited reveal with re-authentication, sensitive-data finder, export watermarking |
| Log and trace tooling slows production | Medium | sampling, overhead budget with automatic back-off, bounded reads, time-boxed verbose modes |
| Debug or replay features cause real side effects | High | replay only on test sites, production-flag refusal, allowlisted diagnostics, no arbitrary code console |
