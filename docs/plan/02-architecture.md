## 2. Architecture

```
admin_utils/
├── admin_utils/
│   ├── hooks.py                 # add_to_apps_screen, doc_events, scheduler, permissions
│   ├── api/                     # whitelisted endpoints, one module per feature
│   ├── core/                    # compat layer (v15/v16), audit, guards, feature flags
│   ├── services/                # business logic (no frappe.whitelist here)
│   ├── doctype/                 # Admin Utils Settings, Permission Level, Job Log ...
│   ├── patches/                 # versioned migrations
│   ├── fixtures/                # roles, role profiles, default level matrices
│   ├── www/manage.py|html       # SPA entry (/manage)
│   └── tests/                   # unit, integration, security, perf
├── frontend/                    # Vite + Vue 3 + frappe-ui + Tailwind
│   ├── src/{pages,components,composables,stores,router,i18n,api}
│   └── tests/{unit,component,e2e}
├── .github/workflows/           # CI matrix v15 × v16
└── docs/
```

**Layering rule:** `api/` (thin, auth + validation) → `services/` (logic) → `core/compat` (version differences) → Frappe. UI never talks to anything except `api/`.

**Feature modules:** each utility = a Python subpackage + a Vue route group + a `<Feature> Settings` doctype + an on/off flag in `Admin Utils Settings`.

**Generated apps:** the App Builder (BLDR) creates and updates separate custom apps through the allowlisted bench runner and fixed templates. Generated apps live outside this app, are owned by the admin, and are never installed on production without an environment-policy approval.
