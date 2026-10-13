## 1. Vision & Principles

1. **Admin-first**: every utility removes a repetitive, error-prone admin chore.
2. **Non-invasive**: no core monkey-patching, no core JS/CSS overrides. New views, new doctypes, new routes only.
3. **Safe by default**: risky features (bench, site config, fail2ban) are off until explicitly enabled and are allowlist-driven, audited and reversible.
4. **Version-agnostic**: a compatibility layer isolates v15/v16 differences.
5. **Everything tested**: no feature merges without unit + integration tests; user-facing flows get e2e; privileged flows get security tests.
6. **Preview → Apply → Undo**: any bulk change shows a diff first and can be rolled back.
7. **Bilingual**: English/Arabic (RTL) is a first-class requirement, not an afterthought.
8. **Promotable**: anything an admin builds in the UI (customizations, permissions, workspaces, reports, translations) can be exported into a version-controlled custom app and promoted between environments.
9. **Agent-buildable**: every feature has a stable ID, acceptance criteria and a testable contract so AI agents can implement and verify it independently.
10. **Learn by doing**: the product teaches itself. Guided, role-aware, bilingual training with a safe practice sandbox is a core capability, not an add-on.
