from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


POSTGRES_URL = 'postgresql://postgres:admin@localhost/orders'
engine = create_engine(POSTGRES_URL, echo=True)

BaseClass = declarative_base()

Session = sessionmaker()