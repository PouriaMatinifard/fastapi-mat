from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


class Userout(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class PostResp(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: Userout

    class Config:
        orm_mode = True


class PostOutVote(BaseModel):
    Post: PostResp
    votes: int

    class Config:
        orm_mode = True


class user_create(BaseModel):
    email: EmailStr
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Tokendata(BaseModel):
    id: Optional[str] = None

class vote(BaseModel):
    post_id: int
    dir: conint(le=1)

