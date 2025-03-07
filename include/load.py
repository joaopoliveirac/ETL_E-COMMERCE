from sqlalchemy.dialects.postgresql import insert
from db import Base, engine, Sessionlocal
from models import Produto, Cliente, Endereco, Pedido, ProdutoPedido
from transform import produtos, clientes, endreco_cliente, pedidos, produtos_pedidos

def inserir_dados():
    # Criar tabelas no banco (se não existirem)
    Base.metadata.create_all(bind=engine)  
    
    session = Sessionlocal()

    try:
        def inserir(tabela, dados):
            insercao = insert(tabela).values(dados).on_conflict_do_nothing()
            session.execute(insercao)
        
        # Inserir os dados em cada tabela
        inserir(Produto, produtos)
        inserir(Cliente, clientes)
        inserir(Endereco, endreco_cliente)
        inserir(Pedido, pedidos)
        inserir(ProdutoPedido, produtos_pedidos)

        session.commit()

    except Exception as erro:
        session.rollback()
        print(f'Falhou, erro: {erro}')
    
    finally:
        session.close()
