from sqlalchemy.orm import Session
from fastapi import HTTPException
from core import database

def read_todos(db: Session):
    return db.query(database.Todo).all()

def create_todo(title: str, description: str, completed: bool, db: Session):
    todo = database.Todo(title=title, description=description, completed=completed)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update_todo(id: int, title: str, description: str, completed: bool, db: Session):
    todo = db.query(database.Todo).filter(database.Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    if title is not None:
        todo.title = title
    if description is not None:
        todo.description = description
    if completed is not None:
        todo.completed = completed
    
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(id: int, db: Session):
    todo = db.query(database.Todo).filter(database.Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
