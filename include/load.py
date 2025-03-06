from db import Base,engine,Sessionlocal
from models import Produto, Cliente, Endereco, Pedido, ProdutoPedido
from transform import produtos, clientes, endreco_cliente, pedidos, produtos_pedidos

Base.metadata.create_all(bind=engine) #estava dando erro pq eu nao tava importando as classes que criei do models, ai nao tinha nenhuma tabela pra ser criada

session = Sessionlocal()
try:
    session.bulk_insert_mappings(Produto, produtos)
    session.bulk_insert_mappings(Cliente, clientes)
    session.bulk_insert_mappings(Endereco, endreco_cliente)
    session.bulk_insert_mappings(Pedido, pedidos)
    session.bulk_insert_mappings(ProdutoPedido, produtos_pedidos)
    session.commit()
except Exception as erro:
    session.rollback()
    print(f'Erro ao inserir os dados: {erro}')
finally:
    session.close()





