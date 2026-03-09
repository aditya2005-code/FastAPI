from src.task.dtos import TaskSchema , TaskResponseSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.task.model import TaskModel

def create_task(body: TaskSchema, db: Session):
    data = body.model_dump()

    new_task = TaskModel(**data)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def get_tasks(db:Session):
    tasks = db.query(TaskModel).all()
    return tasks

def get_one_task(task_id:int , db:Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        return HTTPException(404 , detail = "Task id is not present")
    return one_task

def  update_task(body:TaskSchema , task_id:int , db:Session):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        return HTTPException(404 , detail = "Task id is not present")
    
    body = body.model_dump()
    for field,value in body.items():
        setattr(one_task,field,value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)

    return one_task

def delete_task(task_id:int , db:Session ):
    one_task=db.query(TaskModel).get(task_id)
    if not one_task:
        return HTTPException(404 , detail = "Task id is not present")
    
    db.delete(one_task)
    db.commit()

    return None

