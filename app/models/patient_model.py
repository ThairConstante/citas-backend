from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, Text
from app.core.config import Base

class Pacientes(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    identificacion = Column(String, unique=True, index=True)
    sexo = Column(String, unique=True, index=True)
    edad = Column(String, unique=True, index=True)
    correo = Column(String, unique=True, index=True)
    telefono = Column(String, unique=True, index=True)