# main.py
from fastapi import FastAPI, HTTPException
from domain.user import User
from pydantic import BaseModel

app = FastAPI()

# Modelo para entrada de dados no POST
class UserRequest(BaseModel):
    nome: str
    idade: int

@app.get("/")
def home():
    return {"mensagem": "🚀 API FastAPI funcionando!"}

@app.get("/hello/{nome}")
def saudacao(nome: str):
    try:
        # Verificando se o nome tem mais de 3 caracteres
        if len(nome) <= 3:
            raise ValueError("O nome precisa ter mais de 3 caracteres!")

        return {"mensagem": f"Olá, {nome}!"}

    except Exception as e:
        # Aqui estamos só imprimindo no console do servidor
        print(f"Ocorreu um erro: {e}")
        return {"mensagem": "❌ Ocorreu um erro no servidor, verifique o console."}

@app.post("/user")
def criar_usuario(user_req: UserRequest):
    try:
        if user_req.idade < 0:
            # exemplo de erro de regra de negócio
            raise HTTPException(status_code=400, detail="Idade não pode ser negativa!")

        user = User(nome=user_req.nome, idade=user_req.idade)
        return {"mensagem": user.apresentar()}

    except HTTPException as e:
        # se já é um erro HTTP, apenas repassa
        raise e
    except Exception as e:
        # erro inesperado → status 500
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
