from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base= declarative_base()
class User(Base):

    __tablename__ = "user" #name of table in database
    id= Column(Integer, primary_key=True,index=True)
    username = Column(String)
    email= Column(String)
    password= Column(String)
    created_at= Column(DateTime)
