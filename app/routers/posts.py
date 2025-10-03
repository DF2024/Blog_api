
import uvicorn

from sqlmodel import select, update
from fastapi import APIRouter, FastAPI, HTTPException, status, Query, Depends
from models import PostBase, Post, PostCreate, PostResponse, User
from db import SessionDep
from typing import List, Optional
from routers import auth
from fastapi.security import OAuth2PasswordBearer
from routers import auth
from fastapi.security import HTTPAuthorizationCredentials

router = APIRouter()

@router.post("/post", response_model = PostResponse)
async def post_create(
    post_data : PostCreate,
    session : SessionDep,
    credentials : HTTPAuthorizationCredentials = Depends(auth.oauth2_scheme)
    ):

    token = credentials.credentials

    payload = auth.decode_access_token(token)
    
    if payload is None:
        raise HTTPException(status_code=401, detail = "Token invalido o expirado")

    username = payload.get("sub")
    statement = select(User).where(User.username == username)
    user = session.exec(statement).first()

    if not user:
        raise HTTPException(status_code = 404, detail = "Usuario no encontrado")

    new_post = Post(
        title = post_data.title,
        content = post_data.content,
        author_id= user.id 
    )
    session.add(new_post)
    session.commit()
    session.refresh(new_post)

    return new_post