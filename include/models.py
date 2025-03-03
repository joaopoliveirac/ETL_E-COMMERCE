#criando as tabelas
from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from db import Base
from datetime import datetime

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer)
    titulo = Column(String)
    preco = Column(Float)
    descricao = Column(String)
    categoria = Column(String)
    imagem = Column(String)

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer)
    nome = Column(String)
    email = Column(String)
    telefone = Column(String)

class Endereco(Base):
    __tablename__ = 'endereço_clientes'
    id = Column(Integer, primary_key = True)
    cliente_id = Column(Integer, ForeignKey('clientes.id') )
    cidade = Column(String)
    rua = Column(String)
    numero = Column(Integer)
    cep = Column(String)

class Pedido(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer)
    cliente_id = Column(Integer) #chave estrangeira, verificar como colocar
    data = Column(DateTime, default = datetime.utcnow)

class ProdutoPedido(Base):
    __tablename__ = 'produtos_pedidos'
    id = Column(Integer, primary_key = True)
    pedido_id = Column(Integer, ForeignKey)
    produto_id = Column(Integer, ForeignKey)
    quantidade = Column(Integer)


    


