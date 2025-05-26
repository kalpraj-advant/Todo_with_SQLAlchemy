from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .functions import read_todos, create_todo, update_todo, delete_todo
from core import database

router = APIRouter()

@router.get("/todos/")
def get_todos(db: Session = Depends(database.get_db)):
    return read_todos(db)

@router.post("/todos/")
def create_todo_endpoint(title: str, description: str = None, completed: bool = False, db: Session = Depends(database.get_db)):
    return create_todo(title, description, completed, db)

@router.put("/todos/{todo_id}")
def update_todo_endpoint(id: int, title: str = None, description: str = None, completed: bool = None, db: Session = Depends(database.get_db)):
    return update_todo(id, title, description, completed, db)

@router.delete("/todos/{todo_id}")
def delete_todo_endpoint(id: int, db: Session = Depends(database.get_db)):
    return delete_todo(id, db)
