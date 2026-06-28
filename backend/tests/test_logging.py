"""Tests for structured logging behavior."""

import json
import logging

from app.core.logging import JsonFormatter, correlation_id_context, request_id_context


def test_json_formatter_includes_context_and_extra_fields() -> None:
    """JSON logs should preserve correlation metadata and useful extra fields."""
    request_token = request_id_context.set("request-123")
    correlation_token = correlation_id_context.set("correlation-456")

    try:
        record = logging.LogRecord(
            name="test",
            level=logging.INFO,
            pathname=__file__,
            lineno=1,
            msg="request_completed",
            args=(),
            exc_info=None,
        )
        record.path = "/health"
        record.duration_ms = 12.5

        payload = json.loads(JsonFormatter().format(record))
    finally:
        request_id_context.reset(request_token)
        correlation_id_context.reset(correlation_token)

    assert payload["message"] == "request_completed"
    assert payload["request_id"] == "request-123"
    assert payload["correlation_id"] == "correlation-456"
    assert payload["path"] == "/health"
    assert payload["duration_ms"] == 12.5
