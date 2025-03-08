import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from datetime import datetime
from include.extract import dados_brutos_produtos, dados_brutos_clientes, dados_brutos_pedidos
from include.transform import transform_produto, transform_cliente, transform_endereco, transform_pedido, transform_produto_pedido
from include.load import inserir_dados
from airflow.decorators import task, dag

@dag(
    dag_id="extrair_api",
    description="pipeline_para_obter_dados_api",
    start_date=datetime(2025, 3, 8),
    schedule="* * * * *",
    catchup=False
)
def api_postgres():

    @task(task_id='extrair_produtos')
    def task_extrair_produtos():
        return dados_brutos_produtos()
    
    @task(task_id='extrair_clientes')
    def task_extrair_clientes():
        return dados_brutos_clientes()
    
    @task(task_id='extrair_pedidos')
    def task_extrair_pedidos():
        return dados_brutos_pedidos()
    
    @task(task_id='transformar_produtos')
    def task_transformar_produtos(dados_produtos):
        return transform_produto(dados_produtos)
    
    @task(task_id='transformar_clientes')
    def task_transformar_clientes(dados_clientes):
        return transform_cliente(dados_clientes)
    
    @task(task_id='transformar_endereco_cliente')
    def task_transformar_endereco_cliente(dados_clientes):
        return transform_endereco(dados_clientes)
    
    @task(task_id='transformar_pedidos')
    def task_transformar_pedidos(dados_pedidos):
        return transform_pedido(dados_pedidos)
    
    @task(task_id='transformar_produtos_pedidos')
    def task_transformar_produtos_pedidos(dados_pedidos, produtos):
        return transform_produto_pedido(dados_pedidos, produtos)
    
    @task(task_id='inserir_dados')
    def task_inserir_dados(produtos, clientes, enderecos, pedidos, produtos_pedidos):
        inserir_dados(produtos, clientes, enderecos, pedidos, produtos_pedidos)

    # Definição das dependências
    t1 = task_extrair_produtos()
    t2 = task_extrair_clientes()
    t3 = task_extrair_pedidos()
    t4 = task_transformar_produtos(t1)
    t5 = task_transformar_clientes(t2)
    t6 = task_transformar_endereco_cliente(t2)
    t7 = task_transformar_pedidos(t3)
    t8 = task_transformar_produtos_pedidos(t3, t4)
    t9 = task_inserir_dados(t4, t5, t6, t7, t8)

    t1 >> t2 >> t3 >> t4 >> t5 >> t6 >> t7 >> t8 >> t9

api_postgres()

        
    


