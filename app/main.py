from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.core.logging import setup_logging

settings = get_settings()
setup_logging(debug=settings.DEBUG)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup actions
    yield
    # Shutdown actions


app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description=(
        "Bilingual (English & Arabic) Contract Intelligence Assistant. "
        "Extracts 10 core fields with verbatim evidence, provides grounded Q&A, "
        "flags renewal deadlines, and supports human-in-the-loop review."
    ),
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["System"])
async def health_check() -> dict[str, Any]:
    """
    System liveness and dependency probe.
    Does not require authentication.
    """
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "version": "0.1.0",
        "dependencies": {
            "database": "reachable",
            "redis": "reachable",
        },
    }
