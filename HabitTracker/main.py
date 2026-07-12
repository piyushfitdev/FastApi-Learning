from datetime import timedelta, date

from fastapi import FastAPI, Depends,HTTPException,status
from fastapi.middleware.cors import CORSMiddleware

import auth
from models import Update_Habit_Log

from auth import get_current_user
from models import User, Habit, Habit_Log,LoginRequest
from database import session,engine
import database_models
from sqlalchemy.orm  import Session
from passlib.context import CryptContext
from typing import Annotated
import dashboard
#----------------------------------------------------------------
app =FastAPI()
app.include_router(auth.router)


database_models.Base.metadata.create_all(bind=engine)


def get_db():
    db= session()
    try:
        yield db
    finally:
        db.close()
db_dependency= Annotated[Session, Depends(get_db)]
user_dependency= Annotated[dict,Depends(get_current_user)]


#Regis
#---------------------------------------------------------------
bcrypt_context= CryptContext(schemes=['bcrypt'], deprecated='auto')
@app.post("/auth/register")
def register(user: User,db: db_dependency):
    user_data= user.model_dump() # converts pydantic in dictionary

    user_data["password"]= bcrypt_context.hash(user.password) #password hashed
    db_user = database_models.Users(**user_data)#put in database model
    db.add(db_user)
    db.commit()
    return user

@app.post("/auth/login", response_model=auth.Token)
async def login(
    login_request: LoginRequest,
    db: db_dependency
):
    user = auth.authenticate_user(
        login_request.username,
        login_request.password,
        db
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = auth.create_access_token(
        user.username,
        user.id,
        timedelta(minutes=20)
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@app.get("/users")
def get_all_users(db:db_dependency,user: user_dependency):

    db_users=db.query(database_models.Users).all()
    return db_users

@app.get("/users/me")
def get_current_user_profile(user: user_dependency,db: db_dependency):
    db_user= db.query(database_models.Users).filter(database_models.Users.id == user["id"]).first()

    return db_user

@app.put("/users/me")
def update_user(update: User,user: user_dependency,db: db_dependency):
    db_user = db.query(database_models.Users).filter(database_models.Users.id == user["id"]).first()
    if db_user:
        db_user.username= update.username
        db_user.email= update.email
        db_user.password= bcrypt_context.hash(update.password)

        db.commit()
        return "User Updated"
    else:
        return "No User Found"

@app.delete("/users/me")
def delete_user(user: user_dependency,
    db: db_dependency):
    db_user = db.query(database_models.Users).filter(database_models.Users.id == user["id"]).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return "User Deleted Successfully"
    else:
        return "No User Found"


#_---------------------------------------------------------------

@app.post("/habits")
def add_task(habit: Habit,user: user_dependency,db: db_dependency):
    habit_data= habit.model_dump() # converts pydantic in dictionary
    db_habit = database_models.Habits(**habit_data)#put in database model
    db_habit.user_id= user["id"]
    db.add(db_habit)
    db.commit()

    #get today's habit id
    db.refresh(db_habit)
    #create today's log
    db_log=database_models.Habit_logs(
        habit_id=db_habit.id,
        date=date.today(),
        status=False
    )
    db.add(db_log)
    db.commit()
    return habit

@app.get("/habits")
def get_habits(user: user_dependency,db: db_dependency):
    db_habits= db.query(database_models.Habits).filter(database_models.Habits.user_id == user["id"]).all()

    if db_habits:
        return db_habits
    return "No Habits Found"

@app.get("/habits/{id}")
def get_habits_by_id(id:int,user: user_dependency,db: db_dependency):
    db_habits = db.query(database_models.Habits).filter(database_models.Habits.user_id == user["id"]
                                                        and database_models.Habits.id == id ).first()
    if db_habits:
        return db_habits
    return "No Habit Found"


@app.put("/habits/{id}")
def update_habits(id:int,update: Habit,user: user_dependency,db: db_dependency ):
    db_habits = db.query(database_models.Habits).filter(database_models.Habits.user_id == user["id"]
                                                        and database_models.Habits.id == id ).first()

    if db_habits:
        db_habits.name = update.name
        db_habits.description= update.description
        db_habits.emoji = update.emoji
        db_habits.color=update.color
        db_habits.frequency = update.frequency
        db.commit()
        return "Habit Updated"
    else:
        return "No Habit Found"

@app.delete("/habits/{id}")
def delete_habit(id:int,user: user_dependency,db: db_dependency):
    db_habit = db.query(database_models.Habits).filter(database_models.Habits.user_id == user["id" ]
                                                     and database_models.Habits.id == id).first()
    if db_habit:
        db.delete(db_habit)
        db.commit()
        return "User Deleted Successfully"
    else:
        return "No User Found"




    #----------------------------------------------------------------------------------------
@app.post("/habit-log/{id}")
def add_log(id:int,log:Habit_Log,user: user_dependency,db: db_dependency ):
    db_user= db.query(database_models.Users).filter(database_models.Users.id == user["id"]).first()
    db_habit = db.query(database_models.Habit_logs).filter(database_models.Habit_logs.habit_id == id ).first()

    if db_habit and db_user:
        habit_data = log.model_dump()  # converts pydantic in dictionary
        db_log = database_models.Habit_logs(**habit_data)  # put in database model
        db_log.habit_id = id
        db.add(db_log)
        db.commit()

        return "Habit Updated"
    else:
        return "No Habit Found"

@app.get("/habit-log")
def get_all_logs(user: user_dependency,db: db_dependency):
    db_logs = (db.query(database_models.Habit_logs).join(database_models.Habits)
                .filter(database_models.Habits.user_id == user["id"]).all())
    return db_logs

@app.get("/habit-log/id")
def get_all_logs(id:int,user: user_dependency, db: db_dependency):
    db_logs = (db.query(database_models.Habit_logs).join(database_models.Habits)
                .filter(database_models.Habits.user_id == user["id"] and database_models.Habit_logs.id == id).all())
    return db_logs

@app.delete("/habit-log/id")
def delete_logs(id:int,user: user_dependency, db: db_dependency):
    db_logs = (db.query(database_models.Habit_logs).join(database_models.Habits)
               .filter(database_models.Habits.user_id == user["id"] and database_models.Habit_logs.id == id).first())
    if db_logs:
        db.delete(db_logs)
        db.commit()
        return "Log Deleted Successfully"
    else:
        return "No Log Found"

@app.put("/habit-log/id")
def update_logs(id:int,log:Update_Habit_Log,user: user_dependency, db: db_dependency):
    db_logs = (db.query(database_models.Habit_logs).join(database_models.Habits)
               .filter(database_models.Habits.user_id == user["id"] and database_models.Habit_logs.id == id).first())
    if db_logs:
        db_logs.status = log.status
        db.commit()
        return "Log Updated"
    else:
        return "No Log Found"


#-------------------------------------------------------------
@app.get("/dashboard")
def get_dashboard(user: user_dependency,db: db_dependency):
    total = dashboard.total_habits(user["id"], db)
    completed=dashboard.completed_today(user["id"], db)
    pending= dashboard.pending_today(total,completed)

    return {
        "total_habits": total,
        "completed_today": completed,
        "pending_today": pending

    }


