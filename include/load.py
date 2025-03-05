import pandas as pd
from db import Base,engine
from models import Produto, Cliente, Endereco, Pedido, ProdutoPedido


Base.metadata.create_all(bind=engine) #aqui ele verifica TODAS as classes que foram registradas como base e cria as tabeças
                                        #estava dando erro pq eu nao tava importando as classes que criei do models, ai nao tinha nenhuma tabela pra ser criada



