import pandas as pd
from datetime import datetime
from extract import dados_brutos_produtos,dados_brutos_clientes, dados_brutos_pedidos

def transform_produto(dados_brutos_produtos):
    produtos = []

    for produto in dados_brutos_produtos:
        produto_transformado = {'id': produto['id'],
                                'titulo': produto['title'],
                                'preco': produto['price'],
                                'descricao': produto['description'],
                                'categoria': produto['category'],
                                'imagem': produto['image']}
    
        produtos.append(produto_transformado)
    df = pd.DataFrame(produtos)
    df.to_csv('PRODUTOS.csv', index=False)

def transform_cliente(dados_brutos_clientes):
    clientes = []

    for cliente in dados_brutos_clientes:
        clientes = []

        for cliente in dados_brutos_clientes:
            cliente_transformado = {'id': cliente['id'],
                                    'nome': cliente['name']['firstname'] + ' ' + cliente['name']['lastname'],
                                    'email': cliente['email'],
                                    'telefone': cliente['phone']}
            
            clientes.append(cliente_transformado)
        df = pd.DataFrame(clientes)
        df.to_csv('CLIENTES.csv', index=False)

def transform_endereco(dados_brutos_clientes):
    endereco_cliente = []

    for cliente in dados_brutos_clientes:
        endereco_transformado = {'cliente_id': cliente['id'],
                                 'cidade': cliente['address']['city'],
                                 'rua': cliente['address']['street'],
                                 'numero': cliente['address']['number'],
                                 'cep': cliente['address']['zipcode']}
        
        endereco_cliente.append(endereco_transformado)
    df = pd.DataFrame(endereco_transformado)
    df.to_csv('ENDERECO_CLIENTE.csv', index=False)

def transform_pedido(dados_brutos_pedidos):
    pedidos = []

    for pedido in dados_brutos_pedidos:
        data = pedido['date']
        data_obj = datetime.fromisoformat(data.replace('Z', '+00:00'))
        data_formatada = data_obj.date()
        pedido_transformado = {'id': pedido['id'],
                               'cliente_id': pedido['userId'],
                               'data': data_formatada}
        
        pedidos.append(pedido_transformado)
    df = pd.DataFrame(pedidos)
    df.to_csv('PEDIDOS.csv', index=False)





