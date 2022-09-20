from model import *

class DaoPartido:
    @classmethod
    def salvar(cls, partido):
        with open('partido.txt', 'a') as arq:
            arq.writelines(partido)
            arq.writelines('\n')

class DaoPrefeito:
    @classmethod
    def salvar(cls, prefeito):
        with open('prefeito.txt', 'a') as arq:
            arq.writelines(prefeito)
            arq.writelines('\n')

class DaoVereador:
    @classmethod
    def salvar(cls, vereador):
        with open('vereador.txt', 'a') as arq:
            arq.writelines(vereador)
            arq.writelines('\n')