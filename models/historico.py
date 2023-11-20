from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from database import db

Base = declarative_base()

class Histórico(db.Model):
    __tablename__ = 'historico'

    id_historico = Column(Integer, primary_key=True, autoincrement=True)
    id_paciente = Column(Integer, foreign_key=True)
    doencaspe = Column(String(100), nullable=False)
    alergias = Column(String(100), nullable=False)
    medicamentos = Column(String(100), default=True)
    cirurgias = Column(String(100), nullable=False)
    hospitalizacoes = Column(String(100), nullable=False)
    imunizacoes = Column(String(100), nullable=False)
    
    
    def def__init__(self, id_historico, id_paciente, doencaspe, alergias, medicamentos, cirurgias, hospitalizacoes, imunizacoes, habitos):
        self.id_historico = id_historico
        self.id_paciente = id_paciente
        self.doencaspe = doencaspe
        self.alergias = alergias
        self.medicamentos = medicamentos
        self.cirurgias = cirurgias
        self.hospitalizacoes = hospitalizacoes
        self.imunizacoes = imunizacoes
    

    def __repr__(self):
        return f"<Paciente(id_historico='{self.id_historico}', id_paciente='{self.id_paciente}', doencaspe='{self.doencaspe}', alergias='{self.alergias}', medicamentos='{self.medicamentos}', cirurgias='{self.cirurgias}', hospitalizacoes='{self.hospitalizacoes}', imunizacoes='{self.imunizacoes}'))>"
    
