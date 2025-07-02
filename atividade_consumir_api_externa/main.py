import requests
import os

headers = {
     "chave-api-dados":os.getenv('TOKEN')
}

url = "https://api.portaldatransparencia.gov.br/api-de-dados/bolsa-familia-disponivel-por-cpf-ou-nis"
cpf = input('CPF:')

params = {
    "codigo":cpf,
    'anoMesReferencia':202401,
    'anoMesCompetencia':202501,
    'pagina':1
}

r = requests.get(url,params=params ,headers=headers)

print(r.status_code)