import requests
import json

def extrair(dados):
    url = f'https://fakestoreapi.com/{dados}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None

def dados_brutos_produtos():
    return extrair('products')

def dados_brutos_pedidos():
    return extrair('carts')

def dados_brutos_clientes():
    return extrair('users')