from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from database import db

Base = declarative_base()

class Consulta(db.Model):
    __tablename__ = 'consulta'

    id_consulta = Column(Integer, primary_key=True, autoincrement=True)
    id_paciente = Column(Integer, foreign_key=True)
    sintomas = Column(String(100), nullable=False)
    exames = Column(String(100), nullable=False)
    diagnosticos = Column(String(100), default=True)
    tratamento = Column(String(100), nullable=False)
    orientacoes = Column(String(100), nullable=False)
    
    
    def def__init__(self, id_consulta, id_paciente, sintomas, exames, diagnosticos, tratamento, orientacoes):
        self.id_consulta = id_consulta
        self.id_paciente = id_paciente
        self.sintomas = sintomas
        self.exames = exames
        self.diagnosticos = diagnosticos
        self.tratamento = tratamento
        self.orientacoes = orientacoes



    def __repr__(self):
        return f"<Paciente(id_consulta='{self.id_consulta}', id_paciente='{self.id_paciente}', sintomas='{self.sintomas}', exames='{self.exames}', diagnosticos='{self.diagnosticos}', tratamento='{self.tratamento}', orientacoes='{self.orientacoes}')>"
    
