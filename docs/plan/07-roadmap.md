## 7. Roadmap

Delivery is organized in **waves**. Because agents can work in parallel, the limiting factor is human review and the sequencing of dependencies, not typing speed. Durations are indicative for a small supervising team and should be adjusted after the first two waves.

The **flagship** is the combination of the Theme Studio, Onboarding Studio, Guidance Engine and Training Academy: the most intuitive way to learn and adopt Frappe. It is delivered early (Wave 3), right after the foundations it depends on.

| Wave | Focus | Main scope | Indicative duration |
|---|---|---|---|
| 0 | Foundation | CORE shell, guard, audit, jobs, compat layer, i18n/RTL; CI matrix v15/v16; agent harness (`AGENTS.md`, spec templates); QAUT-001/002 | 3–4 weeks |
| 1 | Permissions & governance core | PERM P0/P1 (ladder, apply, rollback, matrix, draft-delete rule); GOVN-001…016; SECU-001…005 | 5–6 weeks |
| 2 | Data, monitoring, logs & test studio | DATA core (sandbox scenarios depend on it), MNTR core, **LOGS P0/P1 (log center)**, **DBUG P0/P1 (error debugger)**, NTFY-001…010, TSTD-001…014, INSI-001…004 | 8–9 weeks |
| 3 | **Flagship: experience & training** | 3a: THEM P0/P1 (studio, tokens, accessibility, scoping) and GUID P0/P1 (runtime, anchors, tooltips); 3b: ONBD P0/P1 (studio, recorder, learner overlay, role paths); 3c: TRAIN P0/P1 (paths, sandbox, task verification, quizzes, certificates, trainer console); KNOW-001…007; MOBL-001…003 | 10–12 weeks |
| 4 | Privileged core | BNCH-001…035 (runner, runbooks), CONF-001…017, BKUP-001…015, F2B-001…021, SECU-006…020; external security review | 6–8 weeks |
| 5 | Builders | REPT, WKSP, FORM, PRNT, DASH, IMEX P0/P1 | 8–10 weeks |
| 6 | Code export & promotion | BLDR P0/P1, MIGR P0/P1, TSTD generators, GOVN deployment controls; shipping themes, onboarding flows and courses inside generated apps (THEM-100, ONBD-094, TRAIN-079) | 6–8 weeks |
| 7 | Views & localization | VIEW P0/P1 (Kanban, calendar, Gantt, table), TRNS, remaining MOBL | 8–10 weeks |
| 8 | Automation & integrations | AUTO P0/P1, APIX P0/P1, NTFY advanced, EXTR P1 | 6–8 weeks |
| 9 | Scale & intelligence | PERF, **TRCE P0/P1 (tracing and profiling)**, INSI, MSIT, AIAS P1, remaining P1 across modules | 7–9 weeks |
| 10 | Hardening & GA | performance and accessibility audits, pen-test, docs, migration guides, beta with real sites, 1.0 | 6–8 weeks |
| 11 | Continuous | all P2 items, ordered by usage analytics and risk; quarterly Frappe compatibility sweeps | ongoing |

**Flagship success criteria (measured on pilot sites)**
- A new user completes their first real task with guidance in under 15 minutes.
- An admin builds a 10-step onboarding flow in under 20 minutes without writing code.
- At least 90% of guided steps still match the UI after a Frappe minor upgrade, and the rest are flagged automatically.
- 100% of shipped flows and lessons have reviewed Arabic and English versions.
- Learners who complete the Junior path make measurably fewer entry errors in their first month (tracked with INSI).
- The Theme Studio produces an accessible (AA) branded theme from a logo in under 5 minutes.

**Dependencies to respect**
- GUID needs the CORE shell and THEM tokens; ONBD needs GUID; TRAIN needs ONBD, GUID, DATA scenarios and sandbox isolation.
- Certification that unlocks a permission level needs PERM and GOVN approvals.
- BLDR and BKUP depend on the allowlisted bench runner (BNCH-001…012), so that core lands in Wave 4 before Wave 6.
- MIGR depends on BLDR, GOVN approvals, BKUP snapshots and TSTD gates.
- AUTO depends on the job framework and NTFY; AIAS depends on audit, masking and GOVN policies.
- LOGS and DBUG depend on the CORE structured logger, audit log and masking utility; DBUG reproduction depends on DATA and sandbox environments; TRCE depends on trace-id propagation (TRCE-001) being wired into CORE early.
- Everything depends on Wave 0 (guard, audit, compat layer, CI).

**Release train:** public alpha after Wave 2; **flagship preview** (theme studio, onboarding, academy) after Wave 3, suitable for early training pilots; beta after Wave 6; release candidate after Wave 9; 1.0 after Wave 10. Privileged modules ship behind feature flags that stay off by default.

**Scope control:** P0 and P1 features define 1.0; P2 features are pulled in from the continuous backlog by usage data, risk and available review capacity.
