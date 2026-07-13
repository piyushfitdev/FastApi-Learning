from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base

Base= declarative_base()
class Transaction(Base):

    __tablename__ = "transactions" #name of table in database
    id= Column(Integer, primary_key=True,index=True)
    amount = Column(Float)
    category= Column(String)
    description = Column(String)
    is_income = Column(Boolean)
    date= Column(String)

