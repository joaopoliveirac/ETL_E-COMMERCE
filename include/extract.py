import requests
import json


def extrair(dados):
    url = f'https://fakestoreapi.com/{dados}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"erro na requisição: {response.status_code}")
        return None

dados_brutos = extrair('products')

