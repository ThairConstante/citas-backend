from sqlalchemy.orm import Session
from app.models.doctor_model import Doctores

import app.schemas.doctor_schemas as schemas

def get_doctores(db: Session):
    return db.query(Doctores).all()

def get_doctor(db: Session, doctor_id: int):
    return db.query(Doctores).filter(Doctores.id == doctor_id).first()

def crear_doctor(db: Session, doctor: schemas.DoctorsCreate):
    db_doctor = Doctores(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def actualizar_doctor(db: Session, doctor_id: int, doctor: schemas.DoctorsUpdate):
    db_doctor = db.query(Doctores).filter(Doctores.id == doctor_id).first()
    if db_doctor:
        db_doctor.nombre = doctor.nombre
        db_doctor.identificacion = doctor.identificacion
        db_doctor.especialidad = doctor.especialidad
        db_doctor.correo = doctor.correo
        db.commit()
        db.refresh(db_doctor)
    return db_doctor

def eliminar_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(Doctores).filter(Doctores.id == doctor_id).first()
    if db_doctor:
        db.delete(db_doctor)
        db.commit()
    return db_doctor