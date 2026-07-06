from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base= declarative_base()
class Users(Base):

    __tablename__ = "users" #name of table in database
    id= Column(Integer, primary_key=True,index=True)
    username = Column(String, unique=True)
    hashed_password= Column(String)
