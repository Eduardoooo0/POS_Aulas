from pydantic import BaseModel

class Veiculos(BaseModel):
    nome:str
    marca:str
    modelo:str
    placa:str