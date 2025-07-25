# user.py

class User:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá! Eu sou {self.nome} e tenho {self.idade} anos."
