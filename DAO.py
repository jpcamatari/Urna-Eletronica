from re import X
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from model import *

def retornaSession():
    USUARIO = "root"
    SENHA = "pedromarins"
    HOST = "35.247.197.93"
    BANCO = "UrnaEletronica"
    PORT = "3306"

    CON = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CON, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session = retornaSession()

class Admin():
    @classmethod
    def cadastrarPrefeito(cls, nomeCandidato, numeroCandidato):
        try:
            prefeito = Prefeito(nomePrefeito = nomeCandidato, numeroPrefeito = numeroCandidato)
            session.add(prefeito)
            session.commit()
            session.rollback()
            print("Executado")
        except Exception as e:
            print(f'Ocorreu um erro: {e}')


    @classmethod
    def cadastrarVereador(cls, nomeCandidato, numeroCandidato):
        try:
            vereador = Vereador(nomeVereador = nomeCandidato, numeroVereador = numeroCandidato)
            session.add(vereador)
            session.commit()
            session.rollback()
            print("Executado")
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    @classmethod
    def mostrarVotosPref(cls):
        x = session.query(Prefeito).all()
        for i in x:
            print(f'Candidado: {i.nomePrefeito} | Votos: {i.votosPrefeito}')
    
    @classmethod
    def mostrarVotosVeri(cls):
        x = session.query(Vereador).all()
        for i in x:
            print(f'Candidado: {i.nomeVereador} | Votos: {i.votosVereador}')




class Votar():
    @classmethod
    def votarVereador(cls, escolha):
        try:
            x = session.query(Vereador).filter(Vereador.numeroVereador == escolha).one()
            x.votosVereador += 1 
            session.add(x)
            session.commit()
            print('Voto Contabilizado com Sucesso!')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    @classmethod
    def votarPrefeito(cls, escolha):
        try:
            x = session.query(Prefeito).filter(Prefeito.numeroPrefeito == escolha).one()
            x.votosPrefeito += 1 
            session.add(x)
            session.commit()
            print('Voto Contabilizado com Sucesso!')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

