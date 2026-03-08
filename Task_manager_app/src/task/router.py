from fastapi import APIRouter , Depends
from src.task import controller
from src.task.dtos import TaskSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create")
def create_task(body:TaskSchema , db:Session = Depends(get_db)):
    return controller.create_task(body , db)