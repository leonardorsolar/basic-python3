Perfeito! Vamos montar um **tutorial passo a passo para iniciantes** de como testar a classe `User` localizada em `domain/user.py`, utilizando **Python + Pytest**. Esse tutorial vai desde a **instalação** até a **execução dos testes**, explicando cada etapa de forma simples.

---

## ✅ Tutorial: Testando a classe `User` com Pytest

### 🧩 1. Estrutura do projeto (exemplo)

```
your_project/
├── domain/
│   └── user.py
├── tests/
│   └── test_user.py
├── main.py
├── requirements.txt
```

---

### 🐍 2. Instalando o Pytest

Abra o terminal na raiz do seu projeto e instale o `pytest` com:

```bash
pip install pytest
```

Se quiser salvar no `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

### 👨‍💻 3. Código da sua classe (`domain/user.py`)

Garanta que o conteúdo do seu `user.py` esteja assim:

```python
# domain/user.py

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return f"User(name={self.username}, email={self.email})"

    def get_user_info(self):
        return {
            "username": self.username,
            "email": self.email
        }

    def set_email(self, new_email):
        self.email = new_email
```

---

### 🧪 4. Criando o arquivo de teste (`tests/test_user.py`)

```python
# tests/test_user.py

from domain.user import User

def test_create_user():
    user = User("leo", "leo@gmail.com")
    assert user.username == "leo"
    assert user.email == "leo@gmail.com"

def test_get_user_info():
    user = User("ana", "ana@example.com")
    info = user.get_user_info()
    assert info == {"username": "ana", "email": "ana@example.com"}

def test_set_email():
    user = User("joao", "old@example.com")
    user.set_email("new@example.com")
    assert user.email == "new@example.com"
```

---

### ▶️ 5. Rodando os testes

No terminal, digite:

```bash
pytest
```

Você verá algo como:

```
=========================== test session starts ============================
collected 3 items

tests/test_user.py ...                                               [100%]

============================ 3 passed in 0.10s ============================
```

✅ Todos os testes passaram!

---

### 💡 Dica para organização:

Você pode incluir um `__init__.py` vazio dentro de `domain/` e `tests/` para transformar em pacotes:

```bash
touch domain/__init__.py
touch tests/__init__.py
```

---

### 📌 Dica extra: Testar apenas um arquivo

```bash
pytest tests/test_user.py
```

---

### 🛠️ Erro comum

Se aparecer erro dizendo `ModuleNotFoundError: No module named 'domain'`, rode com:

```bash
PYTHONPATH=. pytest
```

ou crie um arquivo `.env` com:

```
PYTHONPATH=.
```

---

### 🚀 Conclusão

Agora você:

-   Instalou o `pytest`
-   Criou uma classe `User`
-   Escreveu testes simples para suas funções
-   Rodou os testes com sucesso!

# Error

Esse erro aconteceu porque o Python **não está conseguindo localizar o módulo `domain.user`** durante a execução dos testes. Isso é comum quando se tenta importar um módulo fora da raiz reconhecida do Python.

---

## ✅ Soluções para o erro: `ModuleNotFoundError: No module named 'domain'`

### ✅ Solução Rápida (temporária para rodar `pytest`)

Execute o comando abaixo dentro da raiz do seu projeto (onde está a pasta `domain/`):

```bash
PYTHONPATH=. pytest
```

Isso diz ao Python: "considere o diretório atual como raiz de importações".

---

### ✅ Solução Permanente: criar estrutura de pacote

1. **Adicione um `__init__.py` vazio na pasta `domain/` e `tests/`**

```bash
touch domain/__init__.py
touch tests/__init__.py
```

2. **Verifique se sua estrutura está assim**:

```
testespythonFasApi/
├── domain/
│   ├── __init__.py
│   └── user.py
├── tests/
│   ├── __init__.py
│   └── test_user.py
├── main.py
```

---

### ✅ Alternativa (se ainda der erro): use `sys.path`

Altere seu arquivo `test_user.py` para forçar a inclusão da pasta raiz no `sys.path`:

```python
# tests/test_user.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from domain.user import User

def test_create_user():
    user = User("leo", "leo@gmail.com")
    assert user.username == "leo"
    assert user.email == "leo@gmail.com"

def test_get_user_info():
    user = User("ana", "ana@example.com")
    info = user.get_user_info()
    assert info == {"username": "ana", "email": "ana@example.com"}

def test_set_email():
    user = User("joao", "old@example.com")
    user.set_email("new@example.com")
    assert user.email == "new@example.com"
```

---

### ✅ Recomendo: Criar um ambiente de testes limpo

Se for trabalhar com muitos testes, você pode usar um arquivo `pytest.ini` com isso:

```ini
# pytest.ini
[pytest]
pythonpath = .
```

Isso evita ter que passar `PYTHONPATH=. pytest` sempre.

---

### ✅ Teste final

Depois disso tudo, rode novamente:

```bash
pytest
```

Você deve ver:

```
collected 3 items

tests/test_user.py ...                                                                                      [100%]
```

---

Ótima pergunta! Por padrão, o `pytest` **suprime as saídas do `print()`** durante a execução dos testes para manter o terminal limpo. Mas **você pode sim ver os `print()`** de duas maneiras:

---

## ✅ Opção 1: Usar a flag `-s`

Execute seu teste com:

```bash
pytest -s
```

Isso habilita a exibição das saídas `print()` no terminal:

```bash
pytest -s tests/test_user.py
```

---

## ✅ Opção 2: Usar `capfd` para capturar a saída (modo programático)

Se você quiser **testar a saída do `print()`** (exemplo: garantir que algo foi impresso corretamente), use o fixture `capfd` do pytest:

```python
from domain.user import User

def test_create_user(capfd):
    user = User("leo", "leo@gmail.com")
    print(user)

    out, err = capfd.readouterr()
    assert "User(name=leo, email=leo@gmail.com)" in out
    assert user.username == "leo"
    assert user.email == "leo@gmail.com"
```

---

### ✅ Dica Final

Se você quiser **ver os prints e os testes organizados**, use:

```bash
pytest -s -v
```

Saída esperada:

```
test_user.py::test_create_user
User(name=leo, email=leo@gmail.com)
PASSED
```

---

usar `logging` em vez de `print`, o que é mais recomendado em projetos maiores.

