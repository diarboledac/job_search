"""Tests for environment-driven application configuration."""

from pytest import MonkeyPatch

from app.core.config import Settings


def test_settings_use_safe_defaults() -> None:
    """Default settings should support local development without secrets."""
    settings = Settings()

    assert settings.app_name == "CareerPilot-AI"
    assert settings.environment == "local"
    assert settings.debug is False
    assert settings.log_level == "INFO"
    assert settings.cors_origins == ["http://localhost:5173"]


def test_settings_read_prefixed_environment(monkeypatch: MonkeyPatch) -> None:
    """Settings should be overridable through CAREERPILOT-prefixed variables."""
    monkeypatch.setenv("CAREERPILOT_ENVIRONMENT", "test")
    monkeypatch.setenv("CAREERPILOT_DEBUG", "true")
    monkeypatch.setenv("CAREERPILOT_CORS_ORIGINS", '["http://localhost:3000"]')

    settings = Settings()

    assert settings.environment == "test"
    assert settings.debug is True
    assert settings.cors_origins == ["http://localhost:3000"]
