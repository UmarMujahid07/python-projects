from typing import Optional
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Local database setup and model imports
from database import Base, engine, get_db
from models import TaskDB

# Initialize FastAPI app
app = FastAPI()

# Create all database tables based on defined SQLAlchemy models
Base.metadata.create_all(bind=engine)


# Pydantic schema for request body validation
class Task(BaseModel):
    title: str
    is_completed: Optional[bool] = False
    priority: Optional[str] = "Medium"


# Endpoint to create a new task in the database
@app.post("/tasks")
def add_task(task: Task, db: Session = Depends(get_db)):
    new_task = TaskDB(
        title=task.title,
        is_completed=task.is_completed,
        priority=task.priority,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# Endpoint to fetch only pending tasks
# Defined above GET /tasks to maintain explicit route resolution precedence
@app.get("/tasks/pending")
def pending_tasks(db: Session = Depends(get_db)):
    return db.query(TaskDB).filter(TaskDB.is_completed == False).all()


# Endpoint to fetch all tasks from the database
@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(TaskDB).all()