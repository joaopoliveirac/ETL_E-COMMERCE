#criando a conexão com o postgre
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base() #criando uma classe Base, que vou utilizar em todas as tabelas do meu banco
url_postgre = "postgresql://postgres:postgres@host.docker.internal:5439/etl_db" #url de conexao com o banco de dados postgre, que roda no docker
engine = create_engine(url_postgre, echo=True) #create engine cria a conexao com o banco, url_postgre tem as credencias do banco e o echo=true faz com que o sqalchemy imprima todas as queries sql executadas
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #cria uma fabrica de sessoes no banco que permitem realizar operacoes, o bind=engine conecta essa fabrica de sessoes ao postgre. autocommit=false voce tem que dar o commit na mao para seguir com uma transacao

