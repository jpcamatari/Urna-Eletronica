class Partido:
    def __init__(self, sigla):
        self.sigla = sigla


class Prefeito:
    def __init__(self, nome, partido, numero, foto):
        self.nome = nome
        self.partido = partido
        self.numero = numero
        self.foto = foto

class Vereador:
    def __init__(self, nome, partido, numero, foto):
        self.nome = nome
        self.partido = partido
        self.numero = numero
        self.foto = foto
