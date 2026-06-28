# Configuration

CareerPilot-AI uses environment variables for runtime configuration. Secrets must never be committed.

## Backend

Backend variables use the `CAREERPILOT_` prefix and are loaded by `app.core.config.Settings`.

Required local defaults are documented in `backend/.env.example`.

- `CAREERPILOT_APP_NAME`: display name used by the API.
- `CAREERPILOT_ENVIRONMENT`: `local`, `test`, or `production`.
- `CAREERPILOT_DEBUG`: enables framework debug mode locally.
- `CAREERPILOT_API_VERSION`: API version exposed in FastAPI metadata.
- `CAREERPILOT_LOG_LEVEL`: structured logging level.
- `CAREERPILOT_CORS_ORIGINS`: JSON list of allowed frontend origins.

## Frontend

Frontend variables must use Vite's `VITE_` prefix. The current local default is documented in `frontend/.env.example`.

- `VITE_API_BASE_URL`: backend API base URL used by future API clients.

## Environments

- `local`: developer machine defaults.
- `test`: automated test execution.
- `production`: deployed environment with externally managed secrets.
