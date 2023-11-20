from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from database import db

Base = declarative_base()

class Usuário(db.Model):
    __tablename__ = 'usuários'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    senha = Column(String(8), nullable=False)

    def def__init__(self, codigo, senha):
        self.codigo = codigo
        self.senha = senha

    def __repr__(self):
        return f"<Usuário(codigo='{self.codigo}', senha='{self.senha}')>"
