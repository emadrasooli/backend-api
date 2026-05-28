from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.config import settings
from app.database import engine, Base
from app.routers.books import router as books_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables on startup
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_title,
    version=settings.app_version,
    description="BookStore API — GitOps thesis demo application",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["health"])
def health_check():
    return {
        "status": "healthy",
        "environment": settings.app_env,
        "version": settings.app_version,
    }


@app.get("/", tags=["root"])
def root():
    return {
        "message": "GitOps Thesis BookStore API",
        "docs": "/docs",
        "health": "/health",
    }


app.include_router(books_router)
