from fastapi import FastAPI,HTTPException
from models import Carro,Cliente,Reserva
from typing import List


app = FastAPI()

carros: List[Carro] = []
clientes: List[Cliente] = []
reservas: List[Reserva] = []

@app.get("/carros", response_model=List[Carro])
def listar_carros():
    return carros

@app.post("/carros", response_model=Carro)
def adicionar_carro(carro: Carro):
    carros.append(carro)
    return carro

@app.put("/carros/{id}", response_model=Carro)
def atualizar_carro(id: int, carro: Carro):
    for index, c in enumerate(carros):
        if c.id == id:
            carros[index] = carro
            return carro
    raise HTTPException(status_code=404, detail="Carro não encontrado")

@app.delete("/carros/{id}")
def remover_carro(id: int):
    for index, c in enumerate(carros):
        if c.id == id:
            del carros[index]
            return {"message": "Carro removido com sucesso"}
    raise HTTPException(status_code=404, detail="Carro não encontrado")

@app.get("/carros/disponiveis", response_model=List[Carro])
def listar_carros_disponiveis():
    return [carro for carro in carros if carro.disponivel]


@app.get("/clientes", response_model=List[Cliente])
def listar_clientes():
    return clientes

@app.post("/clientes", response_model=Cliente)
def adicionar_cliente(cliente: Cliente):
    clientes.append(cliente)
    return cliente

@app.get("/clientes/{id}", response_model=Cliente)
def buscar_cliente(id: int):
    for cliente in clientes:
        if cliente.id == id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

@app.post("/reservas", response_model=Reserva)
def criar_reserva(reserva: Reserva):
    carro = next((c for c in carros if c.id == reserva.carro_id), None)
    if carro is None:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    if not carro.disponivel:
        raise HTTPException(status_code=400, detail="Carro indisponível")

    
    cliente = next((c for c in clientes if c.id == reserva.cliente_id), None)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    if reserva.data_inicio >= reserva.data_fim:
        raise HTTPException(status_code=400, detail="Data de fim deve ser após a data de início")
    carro.disponivel = False
    reservas.append(reserva)
    return reserva

@app.get("/reservas", response_model=List[Reserva])
def listar_reservas():
    return reservas

@app.delete("/reservas/{id}")
def cancelar_reserva(id: int):
    for index, reserva in enumerate(reservas):
        if reserva.id == id:
            carro = next((c for c in carros if c.id == reserva.carro_id), None)
            if carro:
                carro.disponivel = True
            del reservas[index]
            return {"message": "Reserva cancelada com sucesso"}
    raise HTTPException(status_code=404, detail="Reserva não encontrada")