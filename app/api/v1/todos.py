from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.repositories.todo_repository import (
    read_todos,
    create_todo,
    update_todo,
    delete_todo
)
from app.config.security import get_current_user

router = APIRouter()

@router.get("/todos/")
def get_todos(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return read_todos(db, current_user["id"])

@router.post("/todos/")
def create_todo_endpoint(title: str, description: str = None, completed: bool = False, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return create_todo(title, description, completed, db, current_user["id"])

@router.put("/todos/{todo_id}")
def update_todo_endpoint(todo_id: int, title: str = None, description: str = None, completed: bool = None, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return update_todo(todo_id, title, description, completed, db, current_user["id"])

@router.delete("/todos/{todo_id}")
def delete_todo_endpoint(todo_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return delete_todo(todo_id, db, current_user["id"])