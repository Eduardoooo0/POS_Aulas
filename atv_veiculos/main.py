from fastapi import FastAPI, HTTPException
from typing import List
from models import Veiculos



app = FastAPI()


veiculos:List[Veiculos] = []

@app.get('/veiculos', response_model=List[Veiculos])
def listar_veiculos():
    return veiculos

@app.post("/veiculos", response_model=Veiculos)
def criar_veiculo(veiculo:Veiculos):
    for i in veiculos:
        if i.placa == veiculo.placa:
            raise HTTPException(400,"Já cadastrado")
    veiculos.append(veiculo)
    return veiculo

@app.delete("/veiculos/{nome}",response_model=Veiculos)
def deletar_veiculo(nome:str):
    for id, veiculo in enumerate(veiculos):
        if veiculo.nome == nome:
            veiculos.pop(id)
            return veiculo
    raise HTTPException(404,"Não localizado")

@app.put("/veiculos/{nome}", response_model=Veiculos)
def atualizar_veiculo(nome: str, veiculo: Veiculos):
    for index, v in enumerate(veiculos):
        if v.nome == nome:
            veiculos[index] = veiculo
            return veiculo
    raise HTTPException(status_code=404, detail="veiculo não encontrado")