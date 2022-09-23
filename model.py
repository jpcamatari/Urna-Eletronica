from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "root"
SENHA = "pedromarins"
HOST = "35.247.197.93"
BANCO = "UrnaEletronica"
PORT = "3306"

CON = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CON, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Prefeito(Base):
    __tablename__ = "Prefeito"
    idPrefeito = Column(Integer, primary_key=True)
    nomePrefeito = Column(String(50))
    numeroPrefeito = Column(Integer)
    votosPrefeito = Column(Integer)

class Vereador(Base):
    __tablename__ = "Vereador"
    idVereador = Column(Integer, primary_key=True)
    nomeVereador = Column(String(50))
    numeroVereador = Column(Integer)
    votosVereador = Column(Integer)

Base.metadata.create_all(engine)