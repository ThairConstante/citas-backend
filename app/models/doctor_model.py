from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, Text
from app.core.config import Base

class Doctores(Base):
    __tablename__ = "doctores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    identificacion = Column(String, unique=True, index=True)
    especialidad = Column(String, unique=True, index=True)
    correo = Column(String, unique=True, index=True)