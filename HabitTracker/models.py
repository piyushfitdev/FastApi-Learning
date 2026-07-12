from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    username : str
    email: str
    password:str

class Habit(BaseModel):
    name : str
    description: str
    emoji: str
    color: str
    frequency: str




class Habit_Log(BaseModel):
    status : bool
    habit_id: int
    date: datetime

class Update_Habit_Log(BaseModel):
    status : bool



class LoginRequest(BaseModel):
    username: str
    password: str
