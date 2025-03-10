from sqlalchemy.dialects.postgresql import insert
from .db import Base, engine, Sessionlocal
from .models import Produto, Cliente, Endereco, Pedido, ProdutoPedido
from .transform import transform_produto,transform_cliente,transform_endereco,transform_pedido,transform_produto_pedido
from .extract import dados_brutos_produtos,dados_brutos_clientes, dados_brutos_pedidos

def inserir_dados(produtos,clientes,enderecos,pedidos,produtos_pedidos):
    """Insere dados processados nas respectivas tabelas do banco de dados PostgreSQL.

    Esta função cria as tabelas no banco de dados (caso ainda não existam) e insere 
    os dados transformados nas tabelas correspondentes, garantindo que não haja 
    duplicatas utilizando `on_conflict_do_nothing()`.

    Parâmetros:
    - produtos (list[dict]): Lista de dicionários contendo os dados transformados dos produtos.
    - clientes (list[dict]): Lista de dicionários contendo os dados transformados dos clientes.
    - enderecos (list[dict]): Lista de dicionários contendo os dados transformados dos endereços.
    - pedidos (list[dict]): Lista de dicionários contendo os dados transformados dos pedidos.
    - produtos_pedidos (list[dict]): Lista de dicionários contendo os dados transformados da relação produto-pedido.

    Funcionamento:
    - Cria as tabelas no banco de dados caso elas ainda não existam.
    - Insere os registros utilizando `INSERT ... ON CONFLICT DO NOTHING`, evitando erros de duplicação.
    - Se ocorrer algum erro durante a inserção, a transação é revertida (`rollback`).
    - A sessão com o banco é fechada ao final da operação."""
    Base.metadata.create_all(bind=engine)  
    
    session = Sessionlocal()

    try:
        def inserir(tabela, dados):
            if dados:  
                insercao = insert(tabela).values(dados).on_conflict_do_nothing()
                session.execute(insercao)
        
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
