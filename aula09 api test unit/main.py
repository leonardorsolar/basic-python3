from fastapi import FastAPI
from domain.user import User

app = FastAPI()

# Rota principal
@app.get("/")
def home():
    user = User("leo", "leo@gmail.com")
    print(user)
    return {
        "mensagem": "🚀 API FastAPI funcionando!",
        "user": user.get_user_info()
    }

