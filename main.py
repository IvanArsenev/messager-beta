from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sqlalchemy.orm as sqlorm
from config import *
from classes import *
from typing import Dict

app = FastAPI()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlorm.declarative_base()

@app.get("/tasks", response_model=Dict[str, Dict])
async def get_all_tasks():
    db = SessionLocal()
    try:
        db_tasks = db.query(Task).all()
        if not db_tasks:
            raise HTTPException(status_code=404, detail="Задачи не найдены")

        # Формирование ответа в формате { "Имя задачи": { "id": id, "description": описание, "status": статус } }
        tasks_response = {
            task.name: {
                "id": task.id,
                "description": task.description,
                "status": task.status.value
            }
            for task in db_tasks
        }

        return tasks_response
    finally:
        db.close()

@app.post("/task")
async def post_task(task_request: TaskRequest = None):
    db = SessionLocal()
    try:
        new_task = Task(
            name=task_request.name,
            description=task_request.description,
            status=task_request.status
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return {"detail": "Задача загружена успешно", "task_id": new_task.id}
    finally:
        db.close()