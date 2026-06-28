"""HTTP middleware for request tracing and structured access logs."""

import logging
from time import perf_counter
from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from app.core.logging import correlation_id_context, request_id_context

REQUEST_ID_HEADER = "X-Request-ID"
CORRELATION_ID_HEADER = "X-Correlation-ID"

logger = logging.getLogger("careerpilot.api.requests")


class RequestContextMiddleware(BaseHTTPMiddleware):
    """Attach request and correlation IDs to logs and responses."""

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        """Process a request while preserving correlation metadata."""
        request_id = request.headers.get(REQUEST_ID_HEADER) or str(uuid4())
        correlation_id = request.headers.get(CORRELATION_ID_HEADER) or request_id

        request_token = request_id_context.set(request_id)
        correlation_token = correlation_id_context.set(correlation_id)
        started_at = perf_counter()

        try:
            response = await call_next(request)
        finally:
            duration_ms = round((perf_counter() - started_at) * 1000, 2)
            logger.info(
                "request_completed",
                extra={
                    "method": request.method,
                    "path": request.url.path,
                    "duration_ms": duration_ms,
                },
            )
            request_id_context.reset(request_token)
            correlation_id_context.reset(correlation_token)

        response.headers[REQUEST_ID_HEADER] = request_id
        response.headers[CORRELATION_ID_HEADER] = correlation_id
        return response
