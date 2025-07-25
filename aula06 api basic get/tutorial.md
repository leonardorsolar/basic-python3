# 🚀 Tutorial: Criando sua Primeira API com FastAPI

> Um guia rápido e fácil para rodar uma API local com FastAPI e Uvicorn.

---

## ✅ 1. Crie a pasta do projeto

Abra seu terminal e execute:

```bash
mkdir meu_app
cd meu_app
```

---

## ✅ 2. Crie o arquivo da aplicação

No terminal (ou no VS Code):

```bash
touch main.py
```

E cole o seguinte código dentro do `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

# Rota principal
@app.get("/")
def home():
    return {"mensagem": "🚀 API FastAPI funcionando!"}

# Rota com parâmetro
@app.get("/hello/{nome}")
def saudacao(nome: str):
    return {"mensagem": f"Olá, {nome}!"}
```

http://localhost:8000/hello/leonardo

---

## ✅ 3. Instale as bibliotecas necessárias

Se ainda não tiver um ambiente virtual, crie um:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Agora instale o FastAPI e o servidor:

```bash
pip install fastapi uvicorn
```

---

## ✅ 4. Adicione o arquivo `.gitignore` (opcional, mas recomendado)

Crie um arquivo `.gitignore`:

```bash
touch .gitignore
```

E adicione o seguinte conteúdo:

```
__pycache__/
*.pyc
*.pyo
venv/
.env/
```

---

## ✅ 5. Execute o servidor localmente

No terminal, dentro da pasta `meu_app`, rode:

```bash
uvicorn main:app --reload
```

> Esse comando diz ao Uvicorn para rodar:
>
> -   `main`: o nome do arquivo `main.py`
> -   `app`: a instância do FastAPI
> -   `--reload`: recarrega o servidor automaticamente quando o código muda (ótimo para desenvolvimento)

---

## ✅ 6. Acesse sua API no navegador

-   Endpoint raiz:
    👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

-   Documentação automática:
    👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## ✅ 7. Teste sua API

No navegador ou usando ferramentas como **Insomnia** ou **Postman**:

-   `GET /`
    → Retorna: `{ "mensagem": "🚀 API FastAPI funcionando!" }`

-   `GET /hello/Leonardo`
    → Retorna: `{ "mensagem": "Olá, Leonardo!" }`

---

## ✅ Próximos passos sugeridos

-   Adicionar **POST, PUT, DELETE**
-   Usar **validação de dados com Pydantic**
-   Criar **estruturas de pastas** mais limpas (controllers, services, etc)
-   Implementar testes com `pytest`

---
