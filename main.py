from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sqlalchemy.orm as sqlorm
from config import *
from classes import *

app = FastAPI()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlorm.declarative_base()

@app.get("/test")
async def get_test():
    return {"message": "OK"}

@app.post("/test/{id}")
async def post_test(id: int):
    return {"message": id}