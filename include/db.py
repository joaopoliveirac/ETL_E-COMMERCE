from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
url_postgre = "postgresql://postgres:postgres@localhost:5437/etl_db"
engine = create_engine(url_postgre)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
