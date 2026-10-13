# GUID — In-App Guidance Engine: tasks

Spec: [`35-guidance-engine.md`](../../specs/35-guidance-engine.md) · 50 tasks · done 0


## Core

| ID | P | Wave | Status | Title |
|---|---|---|---|---|
| [GUID-001](GUID-001.md) | P0 | 3 | todo | Overlay runtime with spotlight, step cards, arrows and correct focus management |
| [GUID-002](GUID-002.md) | P0 | 3 | todo | Works inside the app SPA and on selected Frappe desk pages through a supported, non-invasive loader |
| [GUID-003](GUID-003.md) | P0 | 3 | todo | Element targeting by role, label, text and data attributes with fallbacks |
| [GUID-004](GUID-004.md) | P0 | 3 | todo | Anchor self-healing suggestions when the UI changes |
| [GUID-005](GUID-005.md) | P0 | 3 | todo | Event-driven progression (click, input, route change, document event, realtime event) |
| [GUID-006](GUID-006.md) | P1 | 3 | todo | Tooltips and hotspots that are persistent, dismissible or once-per-user |
| [GUID-007](GUID-007.md) | P1 | 3 | todo | Beacons that highlight new or recommended features |
| [GUID-008](GUID-008.md) | P1 | 3 | todo | "This page" help panel with relevant lessons, articles and glossary terms |
| [GUID-009](GUID-009.md) | P1 | 3 | todo | Field-level help showing meaning, example, common mistakes and who normally fills it |
| [GUID-010](GUID-010.md) | P1 | 3 | todo | Form walkthrough generated from doctype metadata (required fields first) |
| [GUID-011](GUID-011.md) | P1 | 3 | todo | Plain-language validation coaching with fix actions |
| [GUID-012](GUID-012.md) | P1 | 3 | todo | "Why can't I do this?" explanations tied to the permission explainer (PERM-027) |
| [GUID-013](GUID-013.md) | P1 | 3 | todo | Role-aware guidance (never teach actions the user cannot perform) |
| [GUID-014](GUID-014.md) | P1 | 3 | todo | Announcement banners and what's-new dialogs with targeting and scheduling |
| [GUID-015](GUID-015.md) | P1 | 3 | todo | Setup checklist widgets for workspaces |
| [GUID-016](GUID-016.md) | P1 | 3 | todo | Empty-state guidance ("no invoices yet, create your first") |
| [GUID-017](GUID-017.md) | P1 | 3 | todo | Keyboard shortcut coach (suggests shortcuts after repeated mouse actions) |
| [GUID-018](GUID-018.md) | P1 | 3 | todo | Task search: type "how to cancel an invoice" and start the matching guided flow |
| [GUID-019](GUID-019.md) | P1 | 3 | todo | Targeting rules by role, company, doctype, first-time use, language and device |
| [GUID-020](GUID-020.md) | P1 | 3 | todo | Frequency caps and fatigue controls so guidance never nags |
| [GUID-021](GUID-021.md) | P1 | 3 | todo | Do-not-disturb and dismiss-forever options with an admin override for critical notices |
| [GUID-022](GUID-022.md) | P1 | 3 | todo | Guidance analytics (views, completions, dismissals) |
| [GUID-023](GUID-023.md) | P1 | 3 | todo | Author preview and test mode on real pages without publishing |
| [GUID-024](GUID-024.md) | P1 | 3 | todo | Safety rule: guidance never auto-clicks, submits or changes data without explicit learner action, except sandbox "do it for me" |
| [GUID-025](GUID-025.md) | P2 | 11 | todo | Action recorder that turns recorded actions into editable steps, with personal-data redaction |
| [GUID-026](GUID-026.md) | P2 | 11 | todo | Animated cursor demonstration ("watch me do it") |
| [GUID-027](GUID-027.md) | P2 | 11 | todo | Narration support with captions (EN/AR) |
| [GUID-028](GUID-028.md) | P2 | 11 | todo | Picture-in-picture video lessons that stay visible while the user works |
| [GUID-029](GUID-029.md) | P2 | 11 | todo | Side-panel helper that answers task questions using approved content only (read-only, links AIAS-017) |
| [GUID-030](GUID-030.md) | P2 | 11 | todo | Context-triggered micro-surveys ("was this form easy to fill?") |
| [GUID-031](GUID-031.md) | P2 | 11 | todo | Guidance for customizations generated from BLDR change sets |
| [GUID-032](GUID-032.md) | P2 | 11 | todo | Flow compatibility tags for v15 and v16 UI differences |
| [GUID-033](GUID-033.md) | P2 | 11 | todo | All guidance elements themed through THEM tokens |
| [GUID-034](GUID-034.md) | P2 | 11 | todo | RTL-correct arrows, spotlights and step cards |
| [GUID-035](GUID-035.md) | P2 | 11 | todo | Accessibility: reduced motion, high contrast, screen-reader announcements |
| [GUID-036](GUID-036.md) | P2 | 11 | todo | Performance budget: runtime lazy-loaded and under 30 KB gzipped until activated |
| [GUID-037](GUID-037.md) | P2 | 11 | todo | Guidance as code: export and import as JSON in app repositories |
| [GUID-038](GUID-038.md) | P2 | 11 | todo | Multi-page flow state that survives reloads and navigation |
| [GUID-039](GUID-039.md) | P2 | 11 | todo | Interrupt handling (session timeout, errors) with graceful resume |
| [GUID-040](GUID-040.md) | P2 | 11 | todo | Guidance for ERPNext modules and custom apps through per-app, per-version anchor packs |
| [GUID-041](GUID-041.md) | P2 | 11 | todo | Shipped anchor packs for common ERPNext screens, versioned per release |
| [GUID-042](GUID-042.md) | P2 | 11 | todo | Post-upgrade detection of UI changes with a list of affected flows |
| [GUID-043](GUID-043.md) | P2 | 11 | todo | Author overlay that reveals all anchors on a page for debugging |
| [GUID-044](GUID-044.md) | P2 | 11 | todo | Conflict resolver when two flows target the same element |
| [GUID-045](GUID-045.md) | P2 | 11 | todo | "Tour of this site" generated from installed apps and workspaces |
| [GUID-046](GUID-046.md) | P2 | 11 | todo | Role-switch preview ("see guidance as a Junior") |
| [GUID-047](GUID-047.md) | P2 | 11 | todo | Nightly Playwright runner that plays every flow to catch broken steps |
| [GUID-048](GUID-048.md) | P2 | 11 | todo | Privacy-preserving, opt-in telemetry aggregates |
| [GUID-049](GUID-049.md) | P2 | 11 | todo | Admin kill switch that disables all guidance instantly |
| [GUID-050](GUID-050.md) | P2 | 11 | todo | Guidance catalog browser (search all tours, tips and checklists) |
