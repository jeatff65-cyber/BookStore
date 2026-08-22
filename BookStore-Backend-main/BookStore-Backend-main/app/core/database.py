from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQLite (local development) does not need the SSL connect arg that hosted
# PostgreSQL providers (Supabase, Render, Neon, etc.) require, but it does
# need check_same_thread disabled for FastAPI's threaded request handling.
if settings.DATABASE_URL.startswith("postgres"):
    connect_args = {"sslmode": "require"}
elif settings.DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
else:
    connect_args = {}

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    connect_args=connect_args,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()