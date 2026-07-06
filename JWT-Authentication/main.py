from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database_models import Users
from database import session,engine
import database_models
from typing import Annotated
from sqlalchemy.orm  import Session
import auth
from auth import get_current_user


app =FastAPI()
app.include_router(auth.router)


database_models.Base.metadata.create_all(bind=engine)


def get_db():
    db= session()
    try:
        yield db
    finally:
        db.close()

db_dependecy= Annotated[Session, Depends(get_db)]
user_dependency= Annotated[dict,Depends(get_current_user)]


@app.get("/", status_code= status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependecy):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    return {"User":user}
