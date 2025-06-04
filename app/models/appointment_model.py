from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, Text
from app.core.config import Base

class Citas(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctores.id"), nullable=False) 
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    estado = Column(Integer, nullable=False)
    observaciones = Column(Text, nullable=True)