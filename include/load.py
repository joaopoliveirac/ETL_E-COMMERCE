from sqlalchemy.dialects.postgresql import insert
from db import Base,engine,Sessionlocal
from models import Produto, Cliente, Endereco, Pedido, ProdutoPedido
from transform import produtos, clientes, endreco_cliente, pedidos, produtos_pedidos

Base.metadata.create_all(bind=engine) #estava dando erro pq eu nao tava importando as classes que criei do models, ai nao tinha nenhuma tabela pra ser criada

session = Sessionlocal()
def carregamento(produtos, clientes, enderecos, pedidos, produtos_pedidos):
    try:
        def inserir(tabela, dados): #on_conflict_do_nothing() impede a inserção de dados que já existem com a mesma chave primária, como TODAS minhas tabelas tem chave primaria, me permite usar essa abordagem de validação
            insercao = insert(tabela).values(dados).on_conflict_do_nothing()
            session.execute(insercao)
        
        inserir(Produto,produtos)
        inserir(Cliente,clientes)
        inserir(Endereco,endreco_cliente)
        inserir(Pedido,pedidos)
        inserir(ProdutoPedido,produtos_pedidos)

        session.commit()

    except Exception as erro:
        session.rollback()
        print(f'Falhou, erro: {erro}')
    finally:
        session.close()

carregar_tudo = carregamento()







