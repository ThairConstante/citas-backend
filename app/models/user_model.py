from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, Text
from app.core.config import Base

class Usuarios(Base):
    __tablename__= "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)