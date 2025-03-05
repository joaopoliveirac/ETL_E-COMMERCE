import pandas as pd
from db import Sessionlocal, engine, Base

Base.metadata.create_all(bind=engine)

csv_file = 'PRODUTOS.csv'
df = pd.read_csv(csv_file)
print(df.head())

