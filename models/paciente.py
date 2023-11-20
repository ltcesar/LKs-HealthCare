from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from database import db

Base = declarative_base()

class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id_paciente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    data_nasc = Column(String(10), nullable=False)
    sexo = Column(Boolean, default=True)
    sexof = Column(Boolean, nullable=False)
    sexom = Column(Boolean, nullable=False)
    cpf = Column(String(14), nullable=False)
    end = Column(String(100), nullable=False)
    tele = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False)
    responsavel = Column(String(100), nullable=False)
    ctt_emergencia = Column(String(15), nullable=False)

    def def__init__(self, id_paciente, nome, data_nasc, sexo, sexof, sexom, cpf, end, tele, email, responsavel, ctt_emergencia):
        self.id_paciente = id_paciente
        self.nome = nome
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.cpf = cpf
        self.end = end
        self.tele = tele
        self.email = email
        self.responsavel = responsavel
        self.ctt = ctt_emergencia

    def __repr__(self):
        return f"<Paciente(id_paciente='{self.id_paciente}', nome='{self.nome}', data_nasc='{self.data_nasc}', sexo='{self.sexo}', cpf='{self.cpf}', end='{self.end}', tele='{self.tele}', email='{self.email}',responsavel='{self.responsavel}',ctt_emergencia='{self.ctt_emergencia}',)>"
    
