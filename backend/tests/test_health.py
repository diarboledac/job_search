"""Tests for API system endpoints."""

from fastapi.testclient import TestClient

from app.core.middleware import CORRELATION_ID_HEADER, REQUEST_ID_HEADER
from app.main import app


def test_health_check_returns_ok() -> None:
    """The health endpoint should confirm that the API process is alive."""
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "api"}


def test_health_check_returns_request_context_headers() -> None:
    """The API should echo request tracing headers for client diagnostics."""
    client = TestClient(app)

    response = client.get(
        "/health",
        headers={
            REQUEST_ID_HEADER: "request-123",
            CORRELATION_ID_HEADER: "correlation-456",
        },
    )

    assert response.headers[REQUEST_ID_HEADER] == "request-123"
    assert response.headers[CORRELATION_ID_HEADER] == "correlation-456"
