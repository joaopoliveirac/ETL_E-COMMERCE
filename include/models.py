#criando as tabelas
from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key = True)
    titulo = Column(String)
    preco = Column(Float)
    descricao = Column(String)
    categoria = Column(String)
    imagem = Column(String)

    pedidos = relationship("ProdutoPedido", back_populates="produto")

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key = True)
    nome = Column(String)
    email = Column(String)
    telefone = Column(String)

    enderecos = relationship("Endereco", back_populates="cliente")
    pedidos = relationship("Pedido", back_populates="cliente")

class Endereco(Base):
    __tablename__ = 'endereco_clientes'
    id = Column(Integer, primary_key = True)
    cliente_id = Column(Integer, ForeignKey('clientes.id') )
    cidade = Column(String)
    rua = Column(String)
    numero = Column(Integer)
    cep = Column(String)

    cliente = relationship("Cliente", back_populates="enderecos")

    __table_args__ = (db.UniqueConstraint('cliente_id', 'cidade', 'rua', 'numero', 'cep', name='unique_endereco_cliente'),) #impede que o mesmo cliente tenha endereços iguais cadastrados duas vezes

class Pedido(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key = True)
    cliente_id = Column(Integer, ForeignKey('clientes.id')) #chave estrangeira, verificar como colocar
    data = Column(DateTime, default = datetime.utcnow)

    cliente = relationship("Cliente", back_populates="pedidos")
    produtos = relationship("ProdutoPedido", back_populates="pedido")

class ProdutoPedido(Base):
    __tablename__ = 'produtos_pedidos'
    id = Column(Integer, primary_key = True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'))
    produto_id = Column(Integer, ForeignKey('produtos.id'))
    quantidade = Column(Integer)

    pedido = relationship("Pedido", back_populates="produtos")
    produto = relationship("Produto", back_populates="pedidos")

    __table_args__ = (db.UniqueConstraint('pedido_id', 'produto_id', name='unique_produto_pedido'),) #impede que o mesmo pedido tenha o o mesmo produto inserido.


    


