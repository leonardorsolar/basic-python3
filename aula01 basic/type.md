## Aula01:

Sim! O Python permite **tipagem estática opcional** usando **type hints** (sugestões de tipo), introduzidas a partir do Python 3.5 (e melhoradas nas versões seguintes). Isso **não impede** a execução do código com tipos errados, mas permite:

-   Autocompletar e validação em IDEs (como VS Code, PyCharm).
-   Verificação com ferramentas como `mypy`, `pyright`, `pylint`.

---

### ✅ Exemplo com type hints:

```python
nome: str = "leonardo"
idade: int = 48
peso: float = 82.5
```

---

### ⚠️ Observação:

Mesmo com os tipos, Python continua sendo uma linguagem **dinamicamente tipada**. Exemplo:

```python
idade: int = "oi"  # Isso não dá erro na execução
```

Para detectar esse erro, use:

```bash
pip install mypy
```

E depois:

```bash
mypy arquivo.py
```

---

### ✅ Exemplo completo com verificação

```python
# arquivo: pessoa.py
nome: str = "leonardo"
idade: int = 48
peso: float = 82.5

print(nome, idade, peso)
```

```bash
mypy pessoa.py
```

Se estiver tudo certo, o `mypy` não retorna nada. Se houver erro de tipo, ele te avisa.

## Aula06:

Em Python, você pode tipar o dicionário de várias formas, dependendo do nível de precisão e da versão do Python que está usando.

---

## ✅ Forma simples (com `dict[str, Any]`)

Essa abordagem é mais genérica:

```python
from typing import Any

pessoa: dict[str, Any] = {
    "nome": "leo",
    "password": 1234,
    "email": "leo@gmail.com"
}

print(pessoa)
print("Dicionário criado:", pessoa)
print("Nome:", pessoa["nome"])
print("Senha:", pessoa["password"])
print("Email:", pessoa["email"])
print("Dicionário manipulado com sucesso.")
```

---

## ✅ Forma recomendada (mais segura e legível) usando `TypedDict`

Se você quiser uma **tipagem precisa por chave**, use `TypedDict` (Python 3.8+ ou `typing_extensions` em versões anteriores):

```python
from typing import TypedDict

class Pessoa(TypedDict):
    nome: str
    password: int
    email: str

pessoa: Pessoa = {
    "nome": "leo",
    "password": 1234,
    "email": "leo@gmail.com"
}

print(pessoa)
print("Dicionário criado:", pessoa)
print("Nome:", pessoa["nome"])
print("Senha:", pessoa["password"])
print("Email:", pessoa["email"])
print("Dicionário manipulado com sucesso.")
```

---

## ✅ Alternativa moderna (Python 3.11+): `dict` com Notação Literal

Se estiver usando Python 3.11+, você pode usar:

```python
pessoa: dict[str, str | int] = {
    "nome": "leo",
    "password": 1234,
    "email": "leo@gmail.com"
}
```

> Mas essa abordagem ainda é menos precisa que `TypedDict`, pois permite qualquer chave string e valores `str | int`.

---

Próximos passos: transformar esse dicionário em uma **classe com métodos** ou mostrar como usar `pydantic` para validação de dados. 

```python
# Aprofundando: leitura

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

tupla: tuple = (1, 2, 3, 4, 5)
print(tupla)

dicionario: dict = {'nome': 'leonardo', 'idade': 30}
print(dicionario)

# constantes:
PI: float = 3.14
print(PI)       

# Tipos de dados:
print(type(name))       # <class 'str'>
print(type(password))   # <class 'int'>
print(type(valor))      # <class 'float'>
print(type(status))     # <class 'bool'>
print(type(lista))      # <class 'list'>
print(type(tupla))      # <class 'tuple'>
print(type(dicionario)) # <class 'dict'>    

# Operadores:
soma: int = 10 + 5
print(soma)  # 15       

subtracao: int = 10 - 5
print(subtracao)  # 5

multiplicacao: int = 10 * 5
print(multiplicacao)  # 50

divisao: float = 10 / 5
print(divisao)  # 2.0   

divisao_inteira: int = 10 // 3
print(divisao_inteira)  # 3 

modulo: int = 10 % 3
print(modulo)  # 1

exponenciacao: int = 10 ** 2
print(exponenciacao)  # 100


# Comparação:
igual: bool = (10 == 10)
print(igual)  # True    

diferente: bool = (10 != 5)
print(diferente)  # True    

maior: bool = (10 > 5)
print(maior)  # True

menor: bool = (10 < 5)
print(menor)  # False

maior_igual: bool = (10 >= 10)
print(maior_igual)  # True

menor_igual: bool = (10 <= 5) 
print(menor_igual)  # False

# Lógicos:
e_logico: bool = (True and False)
print(e_logico)  # False    

ou_logico: bool = (True or False)
print(ou_logico)  # True

nao_logico: bool = not True
print(nao_logico)  # False

# Atribuição:
a: int = 10
b: int = 5
a += b  # a = a + b
print(a)  # 15
a -= b  # a = a - b
print(a)  # 10
a *= b  # a = a * b
print(a)  # 50
a /= b  # a = a / b
print(a)  # 10.0
a //= b  # a = a // b
print(a)  # 2.0
a %= b  # a = a % b
print(a)  # 2.0
a **= b  # a = a ** b
print(a)  # 32.0

# Identidade:
x: int = 10
y: int = 10
print(x is y)  # True
print(x is not y)  # False  

# Membros:
lista_membros: list = [1, 2, 3, 4, 5]
print(3 in lista_membros)  # True
print(6 not in lista_membros)  # True   

# Bitwise:
bitwise_and: int = 10 & 5
print(bitwise_and)  # 0
bitwise_or: int = 10 | 5
print(bitwise_or)  # 15
bitwise_xor: int = 10 ^ 5
print(bitwise_xor)  # 15
bitwise_not: int = ~10
print(bitwise_not)  # -11
bitwise_left_shift: int = 10 << 2
print(bitwise_left_shift)  # 40
bitwise_right_shift: int = 10 >> 2
print(bitwise_right_shift)  # 2

# Membership:
string: str = "Hello, World!"
print('Hello' in string)  # True
print('Python' not in string)  # True

# Type casting: 
numero_str: str = "123"
numero_int: int = int(numero_str)
print(numero_int)  # 123    

numero_float: float = float(numero_str)
print(numero_float)  # 123.0
numero_bool: bool = bool(numero_str)
print(numero_bool)  # True (non-empty string is True)
numero_lista: list = list(numero_str)
print(numero_lista)  # ['1', '2', '3']
numero_tupla: tuple = tuple(numero_str)
print(numero_tupla)  # ('1', '2', '3')
numero_dicionario: dict = {'numero': numero_int}
print(numero_dicionario)  # {'numero': 123}

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

def calcula_media(numeros: list) -> float:
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)

print(calcula_media([10, 20, 30]))  # 20.0

def concatena_strings(*args: str) -> str:
    return ' '.join(args)

print(concatena_strings("Olá", "mundo!"))  # Olá mundo!

def fatorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)
print(fatorial(5))  # 120

def fibonacci(n: int) -> list:
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

