from pydantic_settings import BaseSettings
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

# Empty by default; the real connection string must be provided via the
# DATABASE_URL environment variable (see .env / .env.example).
DEFAULT_DATABASE_URL = "sqlite:///./bookstore.db"


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-super-secret-key-change-me-in-production")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))

    @property
    def CORS_ORIGINS(self) -> List[str]:
        # Origins from the CORS_ORIGINS env var (optional).
        env_origins = [
            o.strip() for o in os.getenv("CORS_ORIGINS", "").split(",") if o.strip()
        ]
        # Production + dev origins that are ALWAYS allowed, merged with the
        # env var so a CORS_ORIGINS override can't accidentally break the
        # deployed frontends.
        default_origins = [
            "http://localhost:3000",
            "http://localhost:3001",
            "http://localhost:5173",
            "http://localhost:8000",
        ]
        seen = set()
        merged = []
        for origin in env_origins + default_origins:
            if origin not in seen:
                seen.add(origin)
                merged.append(origin)
        return merged

    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignore extra env vars not declared as fields (e.g. CORS_ORIGINS)


settings = Settings()

# Detect any obvious placeholder text so we don't try to connect to a
# fake host (e.g. an un-filled .env / env var).
_PLACEHOLDER_MARKERS = (
    "PASSWORD_HERE",
    "YOUR_DATABASE_PASSWORD",
    "YOUR_DATABASE_HOST",
    "YOUR_PASSWORD",
    "REPLACE_ME",
)

# If DATABASE_URL is empty or still has a placeholder, fall back to a LOCAL
# development database (SQLite) so the app can run immediately. Set
# DATABASE_URL to your real PostgreSQL connection string to use the
# production database instead.
if not settings.DATABASE_URL or any(m in settings.DATABASE_URL for m in _PLACEHOLDER_MARKERS):
    print(
        "\n=============================================================\n"
        " WARNING: DATABASE_URL is not configured with real credentials.\n"
        " Falling back to a LOCAL development database (SQLite).\n"
        " To use your real PostgreSQL database, set DATABASE_URL in .env\n"
        "   e.g. postgresql://USER:PASSWORD@HOST:5432/DBNAME\n"
        "=============================================================\n"
    )
    settings.DATABASE_URL = "sqlite:///./bookstore.db"
