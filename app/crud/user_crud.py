from sqlalchemy.orm import Session
from app.models.user_model import Usuarios
import app.schemas
from app.schemas.user_schemas import UserCreate, UserUpdate


def get_usuarios(db: Session):
    return db.query(Usuarios).all()

def get_usuario(db: Session, user_id: int):
    return db.query(Usuarios).filter(Usuarios.id == user_id).first()

def crear_usuario(db: Session, user: UserCreate):
    db_usuario = Usuarios(**user.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def actualizar_usuario(db: Session, user_id: int, user: UserUpdate):
    db_usuario = db.query(Usuarios).filter(Usuarios.id == user_id).first()
    if db_usuario:
        db_usuario.nombre = user.nombre
        db_usuario.username = user.username
        if user.password:
            db_usuario.password = user.password
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def eliminar_usuario(db: Session, user_id: int):
    db_usuario = db.query(Usuarios).filter(Usuarios.id == user_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario