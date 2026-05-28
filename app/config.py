from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    app_env: str = "development"
    database_url: str = "postgresql://appuser:AppPass2026!@localhost:5432/appdb"
    app_title: str = "GitOps Thesis API"
    app_version: str = "1.0.0"
    debug: bool = False

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
