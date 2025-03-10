import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from include.extract import dados_brutos_clientes,dados_brutos_produtos,dados_brutos_pedidos
from include.transform import transform_produto,transform_cliente,transform_endereco,transform_pedido,transform_produto_pedido
from include.load import inserir_dados
from include.db import Base, engine, Sessionlocal
from include.models import Produto, Cliente, Endereco, Pedido, ProdutoPedido
from datetime import datetime
from airflow.decorators import task, dag

@dag(dag_id="etl_ecommerce",
     description="pipeline_para_extrair",
     start_date=datetime(2025,3,9),
     schedule="* * * * *",
     catchup=False)

def pipeline():

    @task(task_id='extrair_dados_produtos')
    def task_extrair_dados_produtos():
        return dados_brutos_produtos()
    
    @task(task_id='extrair_dados_clientes')
    def task_extrair_dados_clientes():
        return dados_brutos_clientes()
    
    @task(task_id='extrair_dados_pedidos')
    def task_extrair_dados_pedidos():
        return dados_brutos_pedidos()
    
    @task(task_id='transformar_produtos')
    def task_transformar_produtos(dados_brutos_produtos):
        return transform_produto(dados_brutos_produtos)
    
    @task(task_id='transformar_clientes')
    def task_transformar_clientes(dados_brutos_clientes):
        return transform_cliente(dados_brutos_clientes)
    
    @task(task_id='transformar_endereco_cliente')
    def task_transformar_endereco_cliente(dados_brutos_clientes_endereco):
        return transform_endereco(dados_brutos_clientes_endereco)
    
    @task(task_id='transformar_pedidos')
    def task_transformar_pedidos(dados_brutos_pedidos):
        return transform_pedido(dados_brutos_pedidos)
    
    @task(task_id='transformar_produtos_pedidos')
    def task_transformar_produtos_pedidos(dados_brutos_pedidos,dados_brutos_produtos):
        return transform_produto_pedido(dados_brutos_pedidos,dados_brutos_produtos)
    
    @task(task_id='inserir')
    def task_inserir(produtos,clientes,endereco,pedidos,produto_pedidos):
        inserir_dados(produtos,clientes,endereco,pedidos,produto_pedidos)
    
    t1 = task_extrair_dados_produtos()
    t2 = task_extrair_dados_clientes()
    t3 = task_extrair_dados_pedidos()
    t4 = task_transformar_produtos(t1)
    t5 = task_transformar_clientes(t2)
    t6 = task_transformar_endereco_cliente(t2)
    t7 = task_transformar_pedidos(t3)
    t8 = task_transformar_produtos_pedidos(t3,t1)
    t9 = task_inserir(t4,t5,t6,t7,t8)

    t1 >> t2 >> t3 >> t4 >> t5 >> t6 >> t7 >> t8 >> t9

pipeline()