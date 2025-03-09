from sqlalchemy.dialects.postgresql import insert
from db import Base, engine, Sessionlocal
from models import Produto, Cliente, Endereco, Pedido, ProdutoPedido
from transform import transform_produto,transform_cliente,transform_endereco,transform_pedido,transform_produto_pedido
from extract import dados_brutos_produtos,dados_brutos_clientes, dados_brutos_pedidos

def inserir_dados(produtos,clientes,enderecos,pedido,produtos_pedidos):
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
        session.close()
produtos = transform_produto(dados_brutos_produtos())
clientes = transform_cliente(dados_brutos_clientes())
endereco= transform_endereco(dados_brutos_clientes())
pedidos = transform_pedido(dados_brutos_pedidos())
produto_pedido = transform_produto_pedido(dados_brutos_pedidos(), dados_brutos_produtos())
inserir_dados(produtos,clientes,endereco,pedidos,produto_pedido)
