# Privileged module review

Applies to: BNCH, CONF, F2B, SECU, BLDR, MIGR, BKUP, AIAS.

**Design gate (before code)**
- [ ] Threat model: who can call it, what the worst misuse is
- [ ] Allowlist / argv-only execution; no shell; no string-built commands
- [ ] Sub-roles and feature flag (off by default)
- [ ] Preview, snapshot, rollback, dry-run where state changes
- [ ] Audit events and reason-required prompts
- [ ] Human approver named in the task Notes

**Merge gate**
- [ ] Security reviewer sign-off (authz matrix, injection, secrets)
- [ ] Two reviewers incl. one human
- [ ] Tests for abuse cases (metacharacters, traversal, replay, privilege escalation)
- [ ] No production credentials or real data used anywhere in the work
