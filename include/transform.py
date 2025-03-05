import pandas as pd
from extract import dados_brutos

def transform_produto(dados_brutos):
    produtos = []

    for produto in dados_brutos:
        produto_transformado = {'id': produto['id'],
                                'titulo': produto['title'],
                                'preco': produto['price'],
                                'descricao': produto['description'],
                                'categoria': produto['category'],
                                'imagem': produto['image']}
    
        produtos.append(produto_transformado)
    df = pd.DataFrame(produtos)
    df.to_csv('PRODUTOS.csv', index=False)

transform_produto(dados_brutos)

