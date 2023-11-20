from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from database import db

Base = declarative_base()



class Evolução_Clínica(db.Model):
    __tablename__ = 'evolução_clinica'

    id_ec = Column(Integer, primary_key=True, autoincrement=True)
    id_paciente = Column(Integer, foreign_key=True)
    data = Column(String(100), nullable=False)
    hora = Column(Integer, nullable=False)
    temperatura = Column(Integer, default=True)
    pressao = Column(Integer, nullable=False)
    freq_card = Column(String(100), nullable=False)
    saturacao = Column(String(15), nullable=False)
    id_exame = Column(Integer, foreign_key=True)
    id_consulta = Column(Integer, foreign_key=True)
    resp_trata = Column(String(100), nullable=False)
    moni_freq = Column(Boolean, nullable=False)
    
    def def__init__(self, id_ec, id_paciente, data, hora, temperatura, pressao, freq_card, saturacao, id_exame, id_consulta, resp_trata, moni_freq):
        self.id_ec = id_ec
        self.id_paciente =id_paciente
        self.data = data
        self.hora = hora
        self.temperatura = temperatura
        self.pressao = pressao
        self.freq_card = freq_card
        self.saturacao = saturacao
        self.id_exame = id_exame
        self.id_consulta = id_consulta
        self.resp_trata = resp_trata
        self.moni_freq = moni_freq


    def __repr__(self):
        return f"<Paciente(id_ec='{self.id_ed}',id_paciente='{self.id_paciente}', data='{self.data}', hora='{self.hora}', temperatura='{self.temperatura}', pressao='{self.pressao}', freq_card='{self.freq_card}', saturacao='{self.saturacao}', id_exame='{self.id_exame}' id_consulta='{self.id_consulta}' resp_trata='{self.resp_trata}' moni_freq='{self.moni_freq}')>"
    
