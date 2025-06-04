from fastapi import APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from app.core.auth_token import decode_token, Annotated
from app.core.config import SessionLocal, engine, get_db

from app.models.appointment_model import Base

import app.crud.appointment_crud as crud
import app.schemas.appointment_schemas as schemas

app = APIRouter()

@app.get("/list", dependencies=[Depends(decode_token)])
def list_appointment(db: Session = Depends(get_db)):
    citas = crud.get_citas(db=db)
    return citas

@app.get("/appointmentId/{cita_id}", dependencies=[Depends(decode_token)], response_model=schemas.CitasBase)
def id_appointment(cita_id: int, db: Session = Depends(get_db)):
    cita = crud.get_cita(db=db, cita_id=cita_id)
    if cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita

@app.post("/create", dependencies=[Depends(decode_token)], response_model=schemas.CitasCreate)
def create_appointment(cita: schemas.CitasCreate, db: Session = Depends(get_db)):
    return crud.crear_cita(db=db, cita=cita)

@app.put("/update/{cita_id}", dependencies=[Depends(decode_token)], response_model=schemas.CitasBase)
def update_appointment(cita_id: int, cita: schemas.CitasUpdate, db: Session = Depends(get_db)):
    cita_actualizada = crud.actualizar_cita(db=db, cita_id=cita_id, cita=cita)
    if cita_actualizada is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita_actualizada

@app.delete("/delete/{cita_id}", dependencies=[Depends(decode_token)], response_model=schemas.CitasBase)
def delete_appointment(cita_id: int, db: Session = Depends(get_db)):
    cita = crud.eliminar_cita(db=db, cita_id=cita_id)
    if cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita