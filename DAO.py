from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from model import Prefeito, Vereador

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

Admin.cadastrarPrefeito('Henrique de Andrade', 15)
