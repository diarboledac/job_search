# Development Tooling

CareerPilot-AI uses automated quality gates to keep each sprint small, reviewable, and runnable.

## Backend

- Ruff checks Python lint rules and import order.
- Black enforces consistent formatting.
- mypy performs static type checking.
- pytest runs backend tests.

Local commands:

```bash
cd backend
ruff check .
black --check .
mypy .
pytest
```

## Frontend

- TypeScript checks frontend types.
- Vitest runs frontend tests.
- Vite verifies production builds.

Local commands:

```bash
cd frontend
npm run typecheck
npm run test
npm run build
```

## Pre-commit

Install hooks from the repository root:

```bash
cd backend
python -m pip install -e ".[dev]"
cd ..
pre-commit install
```

Pre-commit runs Ruff, Ruff format, mypy, and basic file hygiene checks.

## CI

GitHub Actions runs backend linting, formatting checks, typing, tests, and frontend typecheck/test/build.
