import requests
import json

def extrair(dados):
    """
    Essa funcao recebe uma parte da URL específica de qual parte da API quer acessar,
    após receber o valor ela faz uma requisição http do tipo get para a url fornecida,
    caso o retorno seja == 200 ela retorna o arquivo em json   
    """
    url = f'https://fakestoreapi.com/{dados}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None

def dados_brutos_produtos():
    """Passando 'products' para a funcao extrair, falando que que acessar https://fakestoreapi.com/products"""
    return extrair('products')

def dados_brutos_pedidos():
    """Passando 'carts' para a funcao extrair, falando que que acessar https://fakestoreapi.com/carts"""
    return extrair('carts')

def dados_brutos_clientes():
    """Passando 'users' para a funcao extrair, falando que que acessar https://fakestoreapi.com/users"""
    return extrair('users')