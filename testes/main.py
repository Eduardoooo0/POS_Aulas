from fastapi import FastAPI
from models import Usuario
from typing import List

app = FastAPI()

user_db:List[Usuario] = []

@app.get('/user', response_model=List[Usuario])
def listar_user():
    return user_db

@app.post('/user')
def criar_user(usuario:Usuario):
    user_db.append(usuario)
    return 'okay'