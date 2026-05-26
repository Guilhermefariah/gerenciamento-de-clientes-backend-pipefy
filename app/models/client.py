from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    patrimonio = Column(Float, nullable=False)
    tipo_solicitacao = Column(String, nullable=False)
    status = Column(String, nullable=False)