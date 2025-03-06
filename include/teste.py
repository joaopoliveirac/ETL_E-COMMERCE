#testar e conhecer os dados da api

import requests
response = requests.get('https://fakestoreapi.com/carts/3')
dados = response.json()
print(dados['products'])

for i, a in enumerate(dados['products']):
    print(a)