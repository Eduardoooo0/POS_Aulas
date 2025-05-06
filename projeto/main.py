from fastapi import FastAPI, HTTPException
from models import Tarefa
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods="*",
    allow_headers="*",
)


tarefas: List[Tarefa] = []

@app.get('/tarefas', response_model=List[Tarefa])
def listar_tarefas():
    return tarefas


@app.post('/tarefas/', response_model=Tarefa)
def criar_tarefas(tarefa:Tarefa):
    tarefa.id = len(tarefas) + 1
    tarefas.append(tarefa)
    return tarefa



@app.delete('/tarefas/{tarefa_id}', response_model=Tarefa)
def excluir_tarefas(tarefa_id:int):
    for index,tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            del tarefas[index]
            return tarefa
    raise HTTPException(status_code=404, detail='não localizado')