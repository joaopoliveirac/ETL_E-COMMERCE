import pandas as pd
from db import Base,engine
from models import Produto, Cliente, Endereco, Pedido, ProdutoPedido

Base.metadata.create_all(bind=engine) #
                                        #estava dando erro pq eu nao tava importando as classes que criei do models, ai nao tinha nenhuma tabela pra ser criada

csv_file = 'PRODUTOS.csv'
df = pd.read_csv(csv_file)

#print(df.head())

df.to_sql("produtos", engine, if_exists="append", index=False)



