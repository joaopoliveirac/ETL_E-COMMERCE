from sqlalchemy.dialects.postgresql import insert
<<<<<<< HEAD
from include.db import Base, engine, Sessionlocal
from include.models import Produto, Cliente, Endereco, Pedido, ProdutoPedido
=======
from .db import Base, engine, Sessionlocal
from .models import Produto, Cliente, Endereco, Pedido, ProdutoPedido
from .transform import produtos, clientes, endreco_cliente, pedidos, produtos_pedidos
>>>>>>> 51d22f0 (consegui comunicar o postgre com o airflow. falta isso auqi: host.docker.internal)

def inserir_dados(produtos, clientes, enderecos, pedidos, produtos_pedidos):
    # Criar tabelas no banco (se não existirem)
    Base.metadata.create_all(bind=engine)  
    
    session = Sessionlocal()

    try:
        def inserir(tabela, dados):
            if dados:  # Evita erro caso a lista esteja vazia
                insercao = insert(tabela).values(dados).on_conflict_do_nothing()
                session.execute(insercao)
        
        # Inserir os dados recebidos como argumentos
        inserir(Produto, produtos)
        inserir(Cliente, clientes)
        inserir(Endereco, enderecos)
        inserir(Pedido, pedidos)
        inserir(ProdutoPedido, produtos_pedidos)

        session.commit()

    except Exception as erro:
        session.rollback()
        print(f'Falhou, erro: {erro}')
    
    finally:
<<<<<<< HEAD
        session.close()
=======
        session.close()

inserir_dados()
>>>>>>> 51d22f0 (consegui comunicar o postgre com o airflow. falta isso auqi: host.docker.internal)
