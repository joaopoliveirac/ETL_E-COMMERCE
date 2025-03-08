from datetime import datetime
from include.extract import dados_brutos_produtos,dados_brutos_clientes, dados_brutos_pedidos

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
    return produtos

def transform_cliente(dados_brutos_clientes):
    clientes = []

    for cliente in dados_brutos_clientes:
        cliente_transformado = {'id': cliente['id'],
                                'nome': cliente['name']['firstname'] + ' ' + cliente['name']['lastname'],
                                'email': cliente['email'],
                                'telefone': cliente['phone']}
            
        clientes.append(cliente_transformado)
    return clientes

def transform_endereco(dados_brutos_clientes):
    endereco_cliente = []

    for cliente in dados_brutos_clientes:
        endereco_transformado = {'cliente_id': cliente['id'],
                                 'cidade': cliente['address']['city'],
                                 'rua': cliente['address']['street'],
                                 'numero': cliente['address']['number'],
                                 'cep': cliente['address']['zipcode']}
        
        endereco_cliente.append(endereco_transformado)
    return endereco_cliente


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
    return pedidos

def transform_produto_pedido(dados_brutos_pedidos,produtos):
    produtos_pedidos = []

    for pedido in dados_brutos_pedidos:
        for i, produto in enumerate(pedido['products']):
            produtos_pedidos_transformado = {'pedido_id': pedido['id'],
                                             'produto_id': produto['productId'],
                                             'quantidade': produto['quantity'],
                                             'total': produtos[i]['preco'] * produto['quantity']}
            
            produtos_pedidos.append(produtos_pedidos_transformado)
    return produtos_pedidos










