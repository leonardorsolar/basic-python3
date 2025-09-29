from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}


# uvicorn 01main:app --reload
# no navegador:http://127.0.0.1:8005/
# visualizará o objeto {"Hello":"World"}