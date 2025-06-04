from fastapi import APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from app.core.auth_token import decode_token, Annotated
from app.core.config import SessionLocal, engine, get_db

from app.models.patient_model import Base

import app.crud.patient_crud as crud
import app.schemas.patient_schemas as schemas

app = APIRouter()

@app.get("/list", dependencies=[Depends(decode_token)])
def list_patients(db: Session = Depends(get_db)):
    pacientes = crud.get_pacientes(db=db)
    return pacientes

@app.get("/patientId/{paciente_id}", dependencies=[Depends(decode_token)], response_model=schemas.PatientsBase)
def id_patient(paciente_id: int, db: Session = Depends(get_db)):
    paciente = crud.get_paciente(db=db, paciente_id=paciente_id)
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

@app.post("/create", dependencies=[Depends(decode_token)], response_model=schemas.PatientsCreate)
def create_patient(paciente: schemas.PatientsCreate, db: Session = Depends(get_db)):
    return crud.crear_paciente(db=db, paciente=paciente)

@app.put("/update/{paciente_id}", dependencies=[Depends(decode_token)], response_model=schemas.PatientsBase)
def update_patient(paciente_id: int, paciente: schemas.PatientsUpdate, db: Session = Depends(get_db)):
    paciente_actualizado = crud.actualizar_paciente(db=db, paciente_id=paciente_id, paciente=paciente)
    if paciente_actualizado is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente_actualizado

@app.delete("/delete/{paciente_id}", dependencies=[Depends(decode_token)], response_model=schemas.PatientsBase)
def delete_patient(paciente_id: int, db: Session = Depends(get_db)):
    paciente = crud.eliminar_paciente(db=db, paciente_id=paciente_id)
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente