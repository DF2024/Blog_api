import uvicorn

from fastapi import FastAPI, Request
from sqlmodel import select
from routers import auth, crud, posts
from db import SessionDep, lifespan


app = FastAPI(
    lifespan = lifespan
)

app.include_router(crud.router)
app.include_router(posts.router)