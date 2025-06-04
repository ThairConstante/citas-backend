from sqlalchemy.orm import Session
from app.models.appointment_model import Citas

import app.schemas.appointment_schemas as schemas

def get_citas(db: Session):
    return db.query(Citas).all()

def get_cita(db: Session, cita_id: int):
    return db.query(Citas).filter(Citas.id == cita_id).first()

def crear_cita(db: Session, cita: schemas.CitasCreate):
    db_cita = Citas(**cita.dict())
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

def actualizar_cita(db: Session, cita_id: int, cita: schemas.CitasUpdate):
    db_cita = db.query(Citas).filter(Citas.id == cita_id).first()
    if db_cita:
        db_cita.paciente_id = cita.paciente_id
        db_cita.doctor_id = cita.doctor_id
        db_cita.fecha = cita.fecha
        db_cita.hora = cita.hora
        db_cita.estado = cita.estado
        db_cita.observaciones = cita.observaciones
        db.commit()
        db.refresh(db_cita)
    return db_cita

def eliminar_cita(db: Session, cita_id: int):
    db_cita = db.query(Citas).filter(Citas.id == cita_id).first()
    if db_cita:
        db.delete(db_cita)
        db.commit()
    return db_cita