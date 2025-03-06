#testar e conhecer os dados da api

import requests
response = requests.get('https://fakestoreapi.com/carts/1')
dados = response.json()
print(dados)

