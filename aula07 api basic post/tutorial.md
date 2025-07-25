# 🚀 Tutorial Completo: Criando sua Primeira API com FastAPI e Classe Separada

---

## ✅ 1. Crie a pasta do projeto

Abra o terminal e digite:

```bash
mkdir meu_app
cd meu_app
```

---

## ✅ 2. Crie um ambiente virtual

Isso evita instalar pacotes globalmente.

```bash
python3 -m venv venv
```

Ative o ambiente:

-   **Linux/macOS**:

    ```bash
    source venv/bin/activate
    ```

-   **Windows**:

    ```bash
    venv\Scripts\activate
    ```

---

## ✅ 3. Instale as bibliotecas necessárias

```bash
pip install fastapi uvicorn pydantic
```

---

## ✅ 4. Crie a estrutura de arquivos

```bash
touch main.py user.py .gitignore
```

---

## ✅ 5. Crie o arquivo `.gitignore`

```gitignore
# Ignorar virtualenv e cache Python
venv/
__pycache__/
*.pyc
*.pyo
.env
```

---

## ✅ 6. Arquivo `user.py` — classe User

```python
# user.py

class User:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá! Eu sou {self.nome} e tenho {self.idade} anos."
```

---

## ✅ 7. Arquivo `main.py` — aplicação FastAPI

```python
# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from user import User

app = FastAPI()

# Modelo de entrada de dados (validação automática)
class UserRequest(BaseModel):
    nome: str
    idade: int

@app.get("/")
def home():
    return {"mensagem": "🚀 API FastAPI funcionando!"}

@app.get("/hello/{nome}")
def saudacao(nome: str):
    return {"mensagem": f"Olá, {nome}!"}

@app.post("/user")
def criar_usuario(user_req: UserRequest):
    user = User(nome=user_req.nome, idade=user_req.idade)
    return {"mensagem": user.apresentar()}
```

---

## ✅ 8. Execute o servidor

No terminal:

```bash
uvicorn main:app --reload
```

---

## ✅ 9. Teste a API

Abra o navegador:

-   📘 Documentação interativa (Swagger):
    👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

-   Teste o `POST /user` com esse corpo:

```json
{
    "nome": "Leonardo",
    "idade": 25
}
```

-   Resultado esperado:

```json
{
    "mensagem": "Olá! Eu sou Leonardo e tenho 25 anos."
}
```

Ótimo! Vamos aprender como **testar sua API FastAPI via `curl`**, direto do terminal — sem precisar abrir o navegador.

---

## 🚀 Servidor rodando

Antes de tudo, certifique-se de que o servidor esteja **ativo** com:

```bash
uvicorn main:app --reload
```

> O FastAPI estará disponível em: `http://127.0.0.1:8000`

---

## ✅ Testar rotas com `curl`

---

### 🔹 1. **GET /** – Testar a rota principal

```bash
curl http://127.0.0.1:8000/
```

✅ Resultado esperado:

```json
{ "mensagem": "🚀 API FastAPI funcionando!" }
```

---

### 🔹 2. **GET /hello/{nome}** – Saudação com nome

```bash
curl http://127.0.0.1:8000/hello/Leonardo
```

✅ Resultado esperado:

```json
{ "mensagem": "Olá, Leonardo!" }
```

---

### 🔹 3. **POST /user** – Criar usuário (com JSON)

```bash
curl -X POST http://127.0.0.1:8000/user \
-H "Content-Type: application/json" \
-d '{"nome": "Leonardo", "idade": 25}'
```

✅ Resultado esperado:

```json
{ "mensagem": "Olá! Eu sou Leonardo e tenho 25 anos." }
```

---

## 🧠 Explicação dos parâmetros:

| Parâmetro | Explicação                                            |
| --------- | ----------------------------------------------------- |
| `-X POST` | Diz ao `curl` que é uma requisição POST               |
| `-H`      | Cabeçalho HTTP (aqui indicando que o conteúdo é JSON) |
| `-d`      | Dados enviados no corpo da requisição (formato JSON)  |

---

## ✅ 10. Dica bônus: salve dependências

Salve os pacotes para facilitar instalação em outras máquinas:

```bash
pip freeze > requirements.txt
```

Depois, para instalar:

```bash
pip install -r requirements.txt
```

---

## ✅ 11. Possíveis erros e soluções

| Erro                                          | Solução                                                           |
| --------------------------------------------- | ----------------------------------------------------------------- |
| `Import "pydantic" could not be resolved`     | Ative o ambiente virtual e instale com `pip install pydantic`     |
| `ModuleNotFoundError: No module named 'user'` | Verifique se o nome do arquivo está correto e está na mesma pasta |

---

## ✅ Próximos passos

Se quiser evoluir o projeto, posso te mostrar:

-   Como usar **PUT, DELETE, GET por ID**
-   Como organizar com **routers (rotas separadas)**
-   Como conectar a um **banco de dados**
-   Como usar arquitetura limpa (domain, usecase, service...)
