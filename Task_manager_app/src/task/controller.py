from src.task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.task.model import TaskModel

def create_task(body: TaskSchema, db: Session):
    data = body.model_dump()

    new_task = TaskModel(**data)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"status": "task created successfully", "data": new_task}