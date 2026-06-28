# Roadmap

## Milestone 1: Platform Foundation

- Sprint 1: create monorepo structure, initial backend/frontend scaffolds, minimal runnable health checks, baseline README/docs.
- Sprint 2: add configuration strategy, environment variable docs, structured JSON logging design, request/correlation ID plan.
- Sprint 3: add development tooling plan and setup for Ruff, Black, mypy, pytest, pre-commit, and GitHub Actions.

Current Sprint 2 progress:

- environment configuration templates are in place
- backend settings load typed `CAREERPILOT_` variables
- structured JSON logging is in place
- request and correlation IDs are propagated through HTTP responses

Current Sprint 3 progress:

- Ruff, Black, mypy, pre-commit, and GitHub Actions are configured
- backend and frontend quality commands are documented

## Later Milestones

- Milestone 2: PostgreSQL, Redis, Celery, scheduler architecture.
- Milestone 3: identity, JWT authentication, and user ownership.
- Milestone 4: career data model.
- Milestone 5: AI Gateway.
- Milestone 6: AI Agents and async workflows.
- Milestone 7: discovery, pgvector readiness, semantic search, and analytics.
