from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

db_url= "postgresql://postgres:123@localhost:5432/finance"
engine= create_engine(db_url) # connects database with python
session= sessionmaker(autocommit= False, autoflush= False, bind= engine)