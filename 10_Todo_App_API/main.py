from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Local application imports
from auth import (
    create_access_token,
    get_current_user,
    hash_password,
    verify_password,
)
from database import Base, engine, get_db
from models import TodoDB, UserDB

# Initialize FastAPI application instance
app = FastAPI()

# Bind models and generate database tables on startup
Base.metadata.create_all(bind=engine)


# Pydantic schema for user registration requests
class UserCreate(BaseModel):
    username: str
    password: str


# Pydantic schema for task creation requests
class ToDoCreate(BaseModel):
    title: str


# Register new user account with hashed password
@app.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    hash_pass = hash_password(user.password)
    new_user = UserDB(username=user.username, hashed_password=hash_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "id": new_user.id,
        "username": new_user.username,
        "message": "User Registered Successfully",
    }


# Authenticate user credentials and return bearer JWT access token
@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    username = form_data.username
    password = form_data.password
    user = db.query(UserDB).filter(UserDB.username == username).first()

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}


# Create new todo record associated with the authenticated user
@app.post("/todos")
def create_task(
    todo: ToDoCreate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user = db.query(UserDB).filter(UserDB.username == current_user).first()

    new_todo = TodoDB(title=todo.title, owner_id=user.id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


# Fetch all todo items belonging to the authenticated user
@app.get("/todos")
def get_tasks(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user = db.query(UserDB).filter(UserDB.username == current_user).first()
    task = db.query(TodoDB).filter(TodoDB.owner_id == user.id).all()

    return task