# Architecture Overview

`CareerPilot-AI` is planned as a multi-user AI career platform. The system will be built incrementally with Clean Architecture and explicit service boundaries.

## Services

- API service: FastAPI HTTP entrypoint, validation, authentication, and dependency wiring.
- Worker service: future Celery workers for long-running AI, document, discovery, and notification jobs.
- Scheduler service: future periodic workflow triggers.
- AI Gateway: future provider-neutral boundary for OpenAI, Anthropic, Gemini, Ollama, and Azure OpenAI.
- AI Agents: future orchestration layer for autonomous career workflows.

## Dependency Rule

Domain code must remain independent from FastAPI, SQLAlchemy, Redis, Celery, and provider SDKs. Infrastructure adapters depend inward on application and domain contracts.
