#criando a conexão com o postgre
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
url_postgre = "postgresql://postgres:postgres@host.docker.internal:5439/etl_db"
engine = create_engine(url_postgre, echo=True)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

