from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from models import User
from database import session,engine
import database_models
from sqlalchemy.orm  import Session


app =FastAPI()


database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to my web server"



def get_db():
    db= session()
    try:
        yield db
    finally:
        db.close()



@app.get("/user")
def get_all_users(db:Session= Depends(get_db)):

    db_users=db.query(database_models.User).all()
    return db_users

@app.get("/user/{id}")
def get_user_by_id(id: int, db:Session= Depends(get_db)):
    db_user= db.query(database_models.User).filter(database_models.User.id == id).first()
    if db_user:
        return db_user
    return "User not found"

@app.post("/user")
def add_user(user: User,db:Session= Depends(get_db)):
    db.add(database_models.User(**user.model_dump()))
    db.commit()
    return user

@app.put("/user/{id}")
def update_user(id: int, user:User,db:Session= Depends(get_db)):
    db_user = db.query(database_models.User).filter(database_models.User.id == id).first()
    if db_user:
        db_user.username= user.username
        db_user.email= user.email
        db_user.password= user.password
        db_user.created_at= user.created_at
        db.commit()
        return "User Added"
    else:
        return "No User Found"

@app.delete("/user/{id}")
def delete_product(id: int,db:Session= Depends(get_db)):
    db_user = db.query(database_models.User).filter(database_models.User.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return "User Deleted Successfully"
    else:
        return "No User Found"