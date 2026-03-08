from fastapi import FastAPI
from src.utils.db import engine , Base
from src.task.model import TaskModel
from src.task.router import task_routes

Base.metadata.create_all(engine)

app = FastAPI(title = "Task Manager App")
app.include_router(task_routes)
