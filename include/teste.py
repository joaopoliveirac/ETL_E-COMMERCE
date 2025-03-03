#testar e conhecer os dados da api

import requests
response = requests.get('https://fakestoreapi.com/carts')
dados = response.json()
print(dados)