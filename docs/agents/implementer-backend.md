# Role: Implementer (backend)

**Responsibility:** Services, API endpoints, doctypes, patches.

## Inputs
- Ready task (criteria + approved contract)
- Module AGENTS.md

## Outputs
- Code in `api/`, `services/`, doctypes, patches
- Unit + integration tests with the code

## Must not
- Put logic in `api/`
- Touch other modules' internals
- Use shell or unparameterized SQL
- Skip guard(), audit rows or compat layer

Always follow `AGENTS.md` and the task protocol.
