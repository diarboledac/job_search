"""Application configuration loaded from environment variables."""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

Environment = Literal["local", "test", "production"]


class Settings(BaseSettings):
    """Runtime settings for the API service."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="CAREERPILOT_",
        extra="ignore",
    )

    app_name: str = "CareerPilot-AI"
    environment: Environment = "local"
    debug: bool = False
    api_version: str = "0.1.0"
    log_level: str = "INFO"
    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173"])


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings for dependency injection."""
    return Settings()
