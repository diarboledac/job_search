# Contributing

`CareerPilot-AI` is developed through small, reviewed sprints.

## Workflow

- Keep each change focused on one sprint.
- Add or update tests for changed behavior.
- Update documentation with every sprint.
- Do not refactor unrelated modules.
- Do not hardcode secrets.
- Prefer explicit, typed, maintainable code over clever abstractions.

## Quality

Run the relevant quality gates before submitting changes:

```bash
cd backend
ruff check .
black --check .
mypy .
pytest
```

```bash
cd frontend
npm run typecheck
npm run test
npm run build
```

Use `pre-commit install` after installing backend development dependencies.

## Technical Review

Every completed sprint must include a technical review covering architecture, code quality, security, scalability, maintainability, tests, documentation, and overall quality.
