# CareerPilot-AI

`CareerPilot-AI` is an AI-powered career platform for managing profiles, job opportunities, applications, analytics, and future autonomous AI workflows.

This repository is being built incrementally as a production-oriented SaaS platform. The first milestone establishes the runnable project foundation before deeper infrastructure, identity, data, and AI features are added.

## Current Sprint

Milestone 1, Sprint 1 is implemented:

- minimal FastAPI backend with a health endpoint
- minimal React/Vite frontend shell
- baseline monorepo folder structure
- initial tests for backend and frontend
- architecture, roadmap, and contribution documentation

## Architecture Direction

The platform will use Clean Architecture with clear boundaries between:

- API service
- background workers
- scheduler
- AI Gateway
- AI Agents
- PostgreSQL persistence
- Redis coordination and caching

Long-running work such as AI analysis, resume generation, notifications, and scheduled discovery must run outside HTTP requests.

## Local Development

Copy the relevant example files before running services that need environment values:

```bash
cp .env.example .env
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

### Backend

```bash
cd backend
python -m pip install -e ".[dev]"
ruff check .
black --check .
mypy .
python -m pytest
uvicorn app.main:app --reload
```

Backend health check:

```bash
GET http://localhost:8000/health
```

### Frontend

```bash
cd frontend
npm install
npm run typecheck
npm run test
npm run build
npm run dev
```

Frontend dev server:

```bash
http://localhost:5173
```

## Documentation

- [Architecture Overview](docs/architecture/overview.md)
- [Configuration](docs/architecture/configuration.md)
- [Observability](docs/architecture/observability.md)
- [Development Tooling](docs/architecture/development-tooling.md)
- [Implementation Rules](docs/architecture/implementation-rules.md)
- [Roadmap](docs/roadmap/roadmap.md)
- [GitHub Issues](docs/github-issues.md)
- [Contributing](CONTRIBUTING.md)

## Delivery Rule

Implementation is sprint-gated. Only one sprint is implemented per iteration, and every sprint must leave the project runnable with tests and documentation updates.
