from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlmodel import Session, create_engine, SQLModel
from typing import Annotated

sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"
engine = create_engine(sqlite_url)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app : FastAPI):
    SQLModel.metadata.create_all(engine)
    yield