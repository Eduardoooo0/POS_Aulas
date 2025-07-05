import requests
import os

headers = {
    "chave-api-dados":os.getenv('TOKEN')
}


def consultar_bolsa_familia_por_cpf_ou_nis(cpf_ou_nis):
            url = "https://api.portaldatransparencia.gov.br/api-de-dados/bolsa-familia-disponivel-por-cpf-ou-nis"

            params = {
                "codigo":int(cpf_ou_nis),
                'anoMesReferencia':202401,
                'anoMesCompetencia':202501,
                'pagina':1
            }

            r = requests.get(url,params=params ,headers=headers)

            print(f'\nCódigo:{r.status_code}\nResposta:{r.json()}\n')


def consultar_bolsa_familia_por_municipio(mes_ano,codigo_ibge):
            url = "https://api.portaldatransparencia.gov.br/api-de-dados/bolsa-familia-por-municipio"
            
            params = {
                "mesAno":int(mes_ano),
                'codigoIbge':codigo_ibge,
                'pagina':1
            }

            r = requests.get(url,params=params ,headers=headers)

            print(f'\nCódigo:{r.status_code}\nResposta:{r.json()}\n')

def consultar_garantia_safra_por_cpf_ou_nis(cpf_ou_nis):
        url = "https://api.portaldatransparencia.gov.br/api-de-dados/safra-codigo-por-cpf-ou-nis"
            
        params = {
            'codigo':cpf_ou_nis,
            'pagina':1
        }

        r = requests.get(url,params=params ,headers=headers)

        print(f'\nCódigo:{r.status_code}\nResposta:{r.json()}\n')

def consultar_seguro_defeso_por_cpf_ou_nis(cpf_ou_nis):
        url = "https://api.portaldatransparencia.gov.br/api-de-dados/seguro-defeso-codigo"
            
        params = {
            'codigo':cpf_ou_nis,
            'pagina':1
        }

        r = requests.get(url,params=params ,headers=headers)

        print(f'\nCódigo:{r.status_code}\nResposta:{r.json()}\n')
        











def consultar_servidor_do_poder_executivo_por_cpf(cpf):
        url = "https://api.portaldatransparencia.gov.br/api-de-dados/servidores"
        
        params = {
            'cpf':cpf,
            'pagina':1
        }

        r = requests.get(url,params=params,headers=headers)
        print(f'\nCódigo:{r.status_code}\nResposta:{r.json()}\n')