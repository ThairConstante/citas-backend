from fastapi import APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from app.core.auth_token import decode_token, Annotated
from app.core.config import SessionLocal, engine, get_db

from app.models.doctor_model import Base

import app.crud.doctor_crud as crud
import app.schemas.doctor_schemas as schemas


app = APIRouter()

@app.get("/list", dependencies=[Depends(decode_token)])
def list_doctors(db: Session = Depends(get_db)):
    doctores = crud.get_doctores(db=db)
    return doctores

@app.get("/doctorId/{doctor_id}", dependencies=[Depends(decode_token)], response_model=schemas.DoctorsBase)
def id_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = crud.get_doctor(db=db, doctor_id=doctor_id)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return doctor

@app.post("/create", dependencies=[Depends(decode_token)], response_model=schemas.DoctorsCreate)
def create_doctor(doctor: schemas.DoctorsCreate, db: Session = Depends(get_db)):
    return crud.crear_doctor(db=db, doctor=doctor)

@app.put("/update/{doctor_id}", dependencies=[Depends(decode_token)], response_model=schemas.DoctorsBase)
def update_doctor(doctor_id: int, doctor: schemas.DoctorsUpdate, db: Session = Depends(get_db)):
    doctor_actualizado = crud.actualizar_doctor(db=db, doctor_id=doctor_id, doctor=doctor)
    if doctor_actualizado is None:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return doctor_actualizado

@app.delete("/delete/{doctor_id}", dependencies=[Depends(decode_token)], response_model=schemas.DoctorsBase)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = crud.eliminar_doctor(db=db, doctor_id=doctor_id)
    if doctor is None:
        raise HTTPException(status_code=404, detail="doctor no encontrado")
    return doctor
