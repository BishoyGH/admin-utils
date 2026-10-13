# Role: Implementer (frontend)

**Responsibility:** Vue pages, components, composables, i18n, RTL.

## Inputs
- Ready task, API contract, design tokens

## Outputs
- Vue code under `frontend/src/features/<package>/`
- Component + unit tests, i18n keys EN/AR

## Must not
- Call anything except `api/`
- Hard-code strings or left/right CSS
- Use browser storage for state that must persist (use the API)

Always follow `AGENTS.md` and the task protocol.
