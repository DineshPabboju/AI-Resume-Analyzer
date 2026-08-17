from contextlib import asynccontextmanager
from fastapi import FastAPI
from .core.database import engine, Base
from .api.v1.router import router as v1_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await engine.dispose()


app = FastAPI(
    title = "Resume Analyzer",
    description = "AI-Powered Resume Analysis",
    lifespan=lifespan
)

app.include_router(v1_router)