import uvicorn
from routers import auth
from fastapi import APIRouter, FastAPI, HTTPException, status, Query
from sqlmodel import select, update
from models import User, UserBase, UserCreate, UserResponse, PostBase, Post, PostCreate, PostResponse
from db import SessionDep
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth_scheme = OAuth2PasswordBearer(tokenUrl = "login")

@router.post("/register", response_model = UserResponse)
async def user_register(
    user_data : UserCreate,
    session : SessionDep
):
    statament = select(User).where(User.username == user_data.username)
    existing_user = session.exec(statament).first()

    if existing_user:
        raise HTTPException(status_code = 400, detail = "El usuario ya existe")

    hashed_pw = auth.hash_password(user_data.password)

    new_user = User(
        username = user_data.username,
        email = user_data.email,
        hashed_password = hashed_pw
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user
