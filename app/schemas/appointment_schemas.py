from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class CitasBase(BaseModel):
    id: int
    paciente_id: int
    doctor_id: int
    fecha: date
    hora: time
    estado: int
    observaciones: Optional[str] = None

class CitasCreate(BaseModel):
    paciente_id: int
    doctor_id: int
    fecha: date
    hora: time
    estado: int
    observaciones: Optional[str] = None

class CitasUpdate(BaseModel):
    paciente_id: int
    doctor_id: int
    fecha: date
    hora: time
    estado: int
    observaciones: Optional[str] = None