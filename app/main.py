from fastapi import FastAPI
from .core.database import create_db_and_tables
from contextlib import asynccontextmanager
from .api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    print("byee")


app = FastAPI(lifespan=lifespan)

app.include_router(api_router)
