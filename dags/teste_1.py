import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from include.extract import dados_brutos_clientes,dados_brutos_produtos,dados_brutos_pedidos
from include.transform import transform_produto,transform_cliente,transform_endereco,transform_pedido,transform_produto_pedido
from include.load import inserir_dados
from include.db import Base, engine, Sessionlocal
from include.models import Produto, Cliente, Endereco, Pedido, ProdutoPedido
from datetime import datetime




def task_extrair_dados_produtos():
    return dados_brutos_produtos()
    

def task_extrair_dados_clientes():
    return dados_brutos_clientes()
    
def task_extrair_dados_pedidos():
    return dados_brutos_pedidos()
    

def task_transformar_produtos(dados_brutos_produtos):
    return transform_produto(dados_brutos_produtos)
    

def task_transformar_clientes(dados_brutos_clientes):
    return transform_cliente(dados_brutos_clientes)
    

def task_transformar_endereco_cliente(dados_brutos_clientes_endereco):
    return transform_endereco(dados_brutos_clientes_endereco)
    

def task_transformar_pedidos(dados_brutos_pedidos):
    return transform_pedido(dados_brutos_pedidos)
    

def task_transformar_produtos_pedidos(dados_brutos_pedidos,dados_brutos_produtos):
    return transform_produto_pedido(dados_brutos_pedidos,dados_brutos_produtos)
    

def task_inserir(produtos,clientes,endereco,pedidos,produto_pedidos):
    inserir_dados(produtos,clientes,endereco,pedidos,produto_pedidos)
    
print(task_transformar_pedidos(task_extrair_dados_pedidos()))

