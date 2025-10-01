from sqlmodel import SQLModel, Field, Relationship, Session
from pydantic import EmailStr
from typing import Optional, List
from enum import Enum

## USUARIOS

class UserBase(SQLModel):
    username : str = Field(default = True)
    email : EmailStr = Field(default = True)
    

class User(UserBase, table= True):
    id : Optional[int] = Field(default = None, primary_key = True)
    hashed_password : str
    
    ## AQUÍ SE REALIZA LA RELACIÓN CON LA TABLA POST
    posts : List["Post"] = Relationship(back_populates="author")


class UserCreate(UserBase):
    password : str

class UserResponse(UserBase):
    id : int

## POSTS

class PostBase(SQLModel):
    title : str
    content : str

class Post(PostBase, table = True):
    id : Optional[int] = Field(default = None, primary_key = True)
    author_id : int = Field(foreign_key="user.id")

    ## AQUÍ SE HACE RELACIÓN CON LA TABLA USER
    author : Optional[User] = Relationship(back_populates = "posts" )


class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id : int
    author_id : int


