# Funções:  
def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"

print(saudacao(name))  # Olá, leonardo!

def soma_numeros(a: int, b: int) -> int:
    return a + b

print(soma_numeros(10, 5))  # 15

def verifica_par(numero: int) -> bool:
    return numero % 2 == 0

print(verifica_par(10))  # True
print(verifica_par(11))  # False

def lista_numeros(numeros: list) -> list:
    return [numero for numero in numeros if isinstance(numero, int)]    

print(lista_numeros([1, 'dois', 3, 'quatro', 5]))  # [1, 3, 5]


class user:
    def __init__(self, name, password) -> dict:
        self.name = name
        self.password = password
        self.objeto = {'name': self.name, 'password': self.password}

    def show(self) -> dict:
        return self.objeto
    
# criando um usuário
user1 = user('leonardo', 123456)
print(user1)
print(user1.name)
print(user1.show())