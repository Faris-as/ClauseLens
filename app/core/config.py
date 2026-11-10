from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Application
    APP_NAME: str = "ClauseLens"
    APP_ENV: str = "development"
    DEBUG: bool = True
    SECRET_KEY: str = "default-insecure-secret-key-change-in-production-min-32-chars"
    API_V1_PREFIX: str = "/api/v1"

    # Database
    DATABASE_URL: str = (
        "postgresql+psycopg://clauselens:clauselens_secret@localhost:5432/clauselens_db"
    )

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # Storage limits
    STORAGE_DIR: str = "/app/storage"
    MAX_UPLOAD_SIZE_MB: int = 25
    MAX_PAGES_LIMIT: int = 200

    # LLM Provider (IFM API / MBZUAI)
    IFM_API_KEY: str = ""
    IFM_BASE_URL: str = "https://api.ifm.ai/v1"
    IFM_MODEL: str = "k2-horizon-large"
    LLM_TEMPERATURE: float = 0.0
    LLM_MAX_TOKENS: int = 1500
    LLM_TIMEOUT_SECONDS: int = 60

    # OCR Engine
    OCR_PRIMARY_ENGINE: str = "easyocr"
    OCR_LANGUAGES: str = "ar,en"
    OCR_GPU_ENABLED: bool = False

    # Security
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    ALGORITHM: str = "HS256"


@lru_cache
def get_settings() -> Settings:
    return Settings()
