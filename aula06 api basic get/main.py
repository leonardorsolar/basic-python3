from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "🚀 API FastAPI funcionando!"}

@app.get("/hello/{nome}")
def saudacao(nome: str):
    return {"mensagem": f"Olá, {nome}!"}
