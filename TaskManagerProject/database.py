from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url= "postgresql://postgres:123@localhost:5432/taskmanager"
engine= create_engine(db_url) # connects database with python
session= sessionmaker(autocommit= False, autoflush= False, bind= engine)