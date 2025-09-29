# 🧑‍🏫 Tutorial: Validação e Tratamento de Erros no FastAPI

## 1. O que é Validação?

Validação é o processo de **verificar se os dados recebidos estão corretos** antes de usá-los no programa.
No FastAPI, usamos principalmente o **Pydantic** para isso.

👉 Exemplo no seu código:

```python
class UserRequest(BaseModel):
    nome: str
    idade: int
```

Isso significa:

-   `nome` precisa ser **texto (string)**.
-   `idade` precisa ser **número inteiro (int)**.

Se alguém mandar:

```json
{ "nome": "Leo", "idade": "abc" }
```

➡️ O FastAPI responde **automaticamente** com erro `422 Unprocessable Entity`.

Ou seja, **nem chega na função** → o FastAPI já faz a validação por você.

---

## 2. Tipos de Tratamento de Erros

No Python puro, aprendemos o `try/except`.
No FastAPI, temos **três formas principais de lidar com erros**:

---

### 🔹 2.1 Tratamento com `print` (didático, para iniciantes)

Usamos quando queremos **mostrar no console** (terminal) o erro, parecido com o que os alunos já viram com `input()` no Python.

```python
@app.get("/hello/{nome}")
def saudacao(nome: str):
    try:
        if len(nome) <= 3:
            raise ValueError("O nome precisa ter mais de 3 caracteres!")
        return {"mensagem": f"Olá, {nome}!"}
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return {"mensagem": "❌ Ocorreu um erro no servidor, verifique o console."}
```

-   Se acessar `/hello/Leo` → erro aparece no **console**.
-   O usuário recebe uma mensagem genérica.

👍 Bom para começar, porque é **idêntico ao Python no terminal**.

---

### 🔹 2.2 Tratamento com `HTTPException` (recomendado em APIs)

Aqui, ao invés de `print`, usamos uma exceção própria do FastAPI.
Serve para retornar um **status code** e uma mensagem clara ao cliente.

```python
@app.post("/user")
def criar_usuario(user_req: UserRequest):
    try:
        if user_req.idade < 0:
            raise HTTPException(status_code=400, detail="Idade não pode ser negativa!")

        user = User(nome=user_req.nome, idade=user_req.idade)
        return {"mensagem": user.apresentar()}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
```

-   Se mandar `{"nome": "Leo", "idade": -5}` → retorna:

```json
{ "detail": "Idade não pode ser negativa!" }
```

👍 Esse é o jeito **profissional** de tratar erros em APIs.

---

### 🔹 2.3 Validação Automática (sem `try/except`)

Quando usamos Pydantic, nem precisamos de `try/except` em alguns casos.
O FastAPI já valida sozinho.

Exemplo:

```json
{ "nome": "Leo", "idade": "abc" }
```

➡️ FastAPI retorna:

```json
{
    "detail": [
        {
            "loc": ["body", "idade"],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
```

👍 Isso evita muito código repetitivo.

---

## 3. Resumindo 🚦

-   **Validação automática (422)** → feita pelo Pydantic.
-   **Tratamento com `print`** → útil para ensinar iniciantes, mostra erro no console.
-   **Tratamento com `HTTPException`** → o jeito certo de responder erros em APIs.
-   **Erros inesperados** → devem ser capturados com `except Exception` para evitar que a aplicação caia.

---
