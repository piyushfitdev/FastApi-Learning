from pydantic import BaseModel
from datetime import datetime

class TransactionBase(BaseModel):
    amount : float
    category: str
    description:str
    is_income: bool
    date:str

class TransactionModel(TransactionBase):
    id:int

    class Config:
        orm_mode=True

