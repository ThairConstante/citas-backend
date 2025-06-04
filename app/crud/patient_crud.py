from sqlalchemy.orm import Session
from app.models.patient_model import Pacientes
import app.schemas.patient_schemas as schemas

def get_pacientes(db: Session):
    return db.query(Pacientes).all()

def get_paciente(db: Session, paciente_id: int):
    return db.query(Pacientes).filter(Pacientes.id == paciente_id).first()

def crear_paciente(db: Session, paciente: schemas.PatientsCreate):
    db_paciente = Pacientes(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def actualizar_paciente(db: Session, paciente_id: int, paciente: schemas.PatientsUpdate):
    db_paciente = db.query(Pacientes).filter(Pacientes.id == paciente_id).first()
    if db_paciente:
        db_paciente.nombre = paciente.nombre
        db_paciente.identificacion = paciente.identificacion
        db_paciente.sexo = paciente.sexo
        db_paciente.edad = paciente.edad
        db_paciente.correo = paciente.correo
        db_paciente.telefono = paciente.telefono
        
        db.commit()
        db.refresh(db_paciente)
    return db_paciente

def eliminar_paciente(db: Session, paciente_id: int):
    db_paciente = db.query(Pacientes).filter(Pacientes.id == paciente_id).first()
    if db_paciente:
        db.delete(db_paciente)
        db.commit()
    return db_paciente