# váriáveis:

name: str = 'leonardo'
print(name)

password: int = 123456
print(password)

valor: float = 1.5
print(valor)

status: bool = True
print(status)

lista: list = [1, 2, 3, 4, 5]
print(lista)

dicionario: dict = {'nome': 'leonardo', 'idade': 30}
print(dicionario)

# constantes:
PI: float = 3.14
print(PI)       

# Tipos de dados:
print(type(name))       # <class 'str'>  

# Operadores:
soma: int = 10 + 5
print(soma)  # 15       


# Comparação:
igual: bool = (10 == 10)
print(igual)  # True    

diferente: bool = (10 != 5)
print(diferente)  # True    

maior: bool = (10 > 5)
print(maior)  # True


# Atribuição:
a: int = 10
b: int = 5
a += b  # a = a + b
print(a)  # 15


# Identidade:
x: int = 10
y: int = 10
print(x is y)  # True
print(x is not y)  # False  

# Membros:
lista_membros: list = [1, 2, 3, 4, 5]
print(3 in lista_membros)  # True
print(6 not in lista_membros)  # True   


# Membership:
string: str = "Hello, World!"
print('Hello' in string)  # True
print('Python' not in string)  # True

# Type casting: 
numero_str: str = "123"
numero_int: int = int(numero_str)
print(numero_int)  # 123    

numero_dicionario: dict = {'numero': numero_int}
print(numero_dicionario)  # {'numero': 123}



