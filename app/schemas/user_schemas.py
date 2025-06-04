from pydantic import BaseModel
from datetime import date, time
from typing import Optional


class UserBase(BaseModel):
    id: int
    nombre: str
    username: str
    password: str

class UserCreate(BaseModel):
    nombre: str
    username: str
    password: str

class UserUpdate(BaseModel):
    nombre: str
    username: str
    password: Optional[str] = None