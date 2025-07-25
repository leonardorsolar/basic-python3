# main.py
from fastapi import FastAPI
from domain.user import User  # importando a classe User
from pydantic import BaseModel  # para validar entrada de dados no POST

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
    return {"mensagem": f"Olá, {nome}!"}

@app.post("/user")
def criar_usuario(user_req: UserRequest):
    user = User(nome=user_req.nome, idade=user_req.idade)
    return {"mensagem": user.apresentar()}
