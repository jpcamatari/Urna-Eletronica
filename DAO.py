from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from model import Prefeito

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

x = Prefeito(nomePrefeito = 'Pedro Marins', numeroPrefeito = 10)
session.add(x)
session.commit()
