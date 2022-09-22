from crypt import methods
from typing_extensions import Self
from model import *
import sqlite3

conn = sqlite3.connect("UrnaEletronica.db")
cur = conn.cursor()


class DaoPartido:
    @classmethod
    def salvar(partido: Partido):
        with conn.execute() as cur:
            cur.execute(f'INSERT INTO Partido values ("{partido}")')
        print("Partido Inserido com Sucesso!")