from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class DoctorsBase(BaseModel):
    id: int
    nombre: str
    identificacion: str
    especialidad: str
    correo: str

class DoctorsCreate(BaseModel):
    nombre: str
    identificacion: str
    especialidad: str
    correo: str

class DoctorsUpdate(BaseModel):
    nombre: str
    identificacion: str
    especialidad: str
    correo: str