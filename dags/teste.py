import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
<<<<<<< HEAD
from include.extract import dados_brutos_produtos,dados_brutos_clientes,dados_brutos_pedidos
from include.transform import produtos,clientes,endreco_cliente,pedidos,produtos_pedidos
=======

from include.extract import dados_brutos_clientes,dados_brutos_produtos
from include.transform import produtos
from include.load import inserir_dados
from include.db import Base, engine, Sessionlocal
from include.models import Produto, Cliente, Endereco, Pedido, ProdutoPedido
from datetime import datetime
from airflow.decorators import task, dag

@dag(dag_id="extrair_dados",
     description="pipeline_para_extrair",
     start_date=datetime(2025,3,9),
     schedule="* * * * *",
     catchup=False)

def pipeline():

    @task(task_id='extrair_dados')
    def task_extrair_dados():
        return dados_brutos_produtos
    
    @task(task_id='transformar')
    def task_transformar():
        return produtos
    
    @task(task_id='inserir')
    def task_inserir():
        return inserir_dados()
    
    t1 = task_extrair_dados()
    t2 = task_transformar()
    t3 = task_inserir()

    t1 >> t2 >> t3

engine
Base.metadata.create_all(engine)
session = Sessionlocal()
pipeline()
    
>>>>>>> 51d22f0 (consegui comunicar o postgre com o airflow. falta isso auqi: host.docker.internal)
