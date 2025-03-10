#criando as tabelas
from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .db import Base
from datetime import datetime

class Produto(Base):
    """Representa a tabela produtos no banco de dados.
    Atributos:
        Representam as colunas no banco.
        pedidos (relationship): Relacionamento com a tabela ProdutoPedido."""
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key = True)
    titulo = Column(String)
    preco = Column(Float)
    descricao = Column(String)
    categoria = Column(String)
    imagem = Column(String)

    pedidos = relationship("ProdutoPedido", back_populates="produto")

class Cliente(Base):
    """Representa a tabela clientes no banco de dados.
    Atributos:
        Representam as colunas no banco.
        pedidos (relationship): Relacionamento com a tabela Pedido."""
    
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key = True)
    nome = Column(String)
    email = Column(String)
    telefone = Column(String)

    enderecos = relationship("Endereco", back_populates="cliente")
    pedidos = relationship("Pedido", back_populates="cliente")

class Endereco(Base):
    """Representa a tabela endereco_clientes no banco de dados.
    Atributos:
        Representam as colunas no banco.
    Restrições:
        - Garante que um cliente não tenha endereços duplicados no banco de dados."""
    __tablename__ = 'endereco_clientes'
    id = Column(Integer, primary_key = True)
    cliente_id = Column(Integer, ForeignKey('clientes.id') )
    cidade = Column(String)
    rua = Column(String)
    numero = Column(Integer)
    cep = Column(String)

    cliente = relationship("Cliente", back_populates="enderecos")

    __table_args__ = (UniqueConstraint('cliente_id', 'cidade', 'rua', 'numero', 'cep', name='unique_endereco_cliente'),) #impede que o mesmo cliente tenha endereços iguais cadastrados duas vezes

class Pedido(Base):
    """Representa a tabela pedidos no banco de dados.
    Atributos:
        Representam as colunas no banco.
        produtos (relationship): Relacionamento com a tabela ProdutoPedido."""
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key = True)
    cliente_id = Column(Integer, ForeignKey('clientes.id')) #chave estrangeira, verificar como colocar
    data = Column(DateTime, default = datetime.utcnow)

    cliente = relationship("Cliente", back_populates="pedidos")
    produtos = relationship("ProdutoPedido", back_populates="pedido")

class ProdutoPedido(Base):
    """
    Representa a tabela produtos_pedidos no banco de dados.
    Atributos:
        Representam as colunas no banco.
    Restrições:
        - Garante que um mesmo pedido não tenha o mesmo produto inserido mais de uma vez."""
    __tablename__ = 'produtos_pedidos'
    id = Column(Integer, primary_key = True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'))
    produto_id = Column(Integer, ForeignKey('produtos.id'))
    quantidade = Column(Integer)
    total = Column(Float)

    pedido = relationship("Pedido", back_populates="produtos")
    produto = relationship("Produto", back_populates="pedidos")

    __table_args__ = (UniqueConstraint('pedido_id', 'produto_id', name='unique_produto_pedido'),) #impede que o mesmo pedido tenha o o mesmo produto inserido.


    


