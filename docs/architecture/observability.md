# Observability

CareerPilot-AI uses structured JSON logs and request correlation metadata from the beginning.

## Request Metadata

The API accepts and returns:

- `X-Request-ID`: unique ID for a single HTTP request.
- `X-Correlation-ID`: ID shared across related API, worker, scheduler, and AI operations.

If a client does not provide these headers, the API generates a request ID and uses it as the correlation ID.

## Logging

Backend logs are JSON formatted and include:

- timestamp
- level
- logger
- message
- request ID
- correlation ID

Sensitive data such as secrets, tokens, resumes, and full AI prompts must not be logged.

## Future Services

Workers, scheduler jobs, and AI Gateway calls must propagate correlation IDs when they are introduced.
