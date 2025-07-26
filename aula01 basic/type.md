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

Próximos passos: transformar esse dicionário em uma **classe com métodos** ou mostrar como usar `pydantic` para validação de dados. Deseja isso?
