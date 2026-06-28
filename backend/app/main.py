"""FastAPI entrypoint for the CareerPilot-AI platform API."""

from fastapi import FastAPI

from app.core.config import get_settings
from app.core.logging import configure_logging
from app.core.middleware import RequestContextMiddleware

settings = get_settings()
configure_logging(settings.log_level)

app = FastAPI(
    title=f"{settings.app_name} API",
    description="API service for the CareerPilot-AI career platform.",
    version=settings.api_version,
    debug=settings.debug,
)
app.add_middleware(RequestContextMiddleware)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    """Return API health status for readiness checks."""
    return {"status": "ok", "service": "api"}
