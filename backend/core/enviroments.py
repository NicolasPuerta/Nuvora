"""Módulo de entornos para el backend."""
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_CONFIG = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    case_sensitive=False,
    extra="ignore",
)


class Enviroments(BaseSettings):
    """Clase de configuración de entornos para el backend."""

    model_config = BASE_CONFIG

    # Configuración de CORS
    url_allowed_cors: list[str]


ENV = Enviroments()
