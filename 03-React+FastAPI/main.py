from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import TransactionBase,TransactionModel
from database_models import Transaction
from database import session,engine
import database_models
from typing import Annotated


app= FastAPI()
origins= [
    "http://localhost:3000",
          ] #only allows this url

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"]
)

def get_db():
    db= session()
    try:
        yield db
    finally:
        db.close()

db_dependency= Annotated[session, Depends(get_db)]

database_models.Base.metadata.create_all(bind=engine)

@app.post("/transactions/")
def create_transaction(transaction: TransactionBase,db: db_dependency):
    db_transaction= database_models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@app.get("/transactions/")
def read_transcations(db: db_dependency):
    transactions= db.query(database_models.Transaction).all()
    return transactions