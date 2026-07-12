from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base

Base= declarative_base()
class Users(Base):

    __tablename__ = "users" #name of table in database
    id= Column(Integer, primary_key=True,index=True)
    username = Column(String)
    email= Column(String)
    password= Column(String)
    created_at= Column(DateTime, default= datetime.utcnow)

class Habits(Base):
    __tablename__ = "habits"  # name of table in database
    id= Column(Integer, primary_key=True,index=True)
    name= Column(String)
    description=Column(String)
    emoji=Column(String)
    color=Column(String)
    frequency=Column(String)
    created_at= Column(DateTime, default= datetime.utcnow)
    is_archived=Column(Boolean,default= False)
    user_id= Column(Integer, ForeignKey("users.id")) #Foreign Key from above table

class Habit_logs(Base):
    __tablename__ = "habit_logs"  # name of table in database
    id= Column(Integer, primary_key=True,index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"))
    status= Column(Boolean, default=False)
    date= Column(DateTime, default= datetime.utcnow)
