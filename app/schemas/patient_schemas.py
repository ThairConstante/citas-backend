from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class PatientsBase(BaseModel):
    id: int
    nombre: str
    identificacion: str
    sexo: str
    edad: str
    correo: str
    telefono: str

class PatientsCreate(BaseModel):
    nombre: str
    identificacion: str
    sexo: str
    edad: str
    correo: str
    telefono: str

class PatientsUpdate(BaseModel):
    nombre: str
    identificacion: str
    sexo: str
    edad: str
    correo: str
    telefono: str