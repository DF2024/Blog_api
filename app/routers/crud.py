import uvicorn
from fastapi import APIRouter, FastAPI, HTTPException, status, Query
from sqlmodel import select, update
from models import User, UserBase, UserCreate, UserResponse, PostBase, Post, PostCreate, PostResponse
from db import SessionDep
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

@router.get("/prueba")
async def prueba():
    return {"messege" : "Hola"}
