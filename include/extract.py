import requests
import json

dados = ''
url = f'https://fakestoreapi.com/{dados}'

def extrair(url):
    response = requests.get(url)
    if response.status_code == 200:
        response.json
        return response.json
    else:
        print(f"erro na requisição: {response.status_code}")
        return None

dados_brutos = extrair()
