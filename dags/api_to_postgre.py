import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from include.extract import dados_brutos_produtos,dados_brutos_clientes,dados_brutos_pedidos
from include.transform import produtos,clientes,endreco_cliente,pedidos,produtos_pedidos
from include.load import inserir_dados


def api_postgres():

    @task(task_id='extrair_produtos')
    def task_extrair_produtos():
        return dados_brutos_produtos
    
    @task(task_id='extrair_clientes')
    def task_extrair_produtos():
        return dados_brutos_clientes
    
    @task(task_id='extrair_pedidos')
    def task_extrair_produtos():
        return dados_brutos_pedidos


