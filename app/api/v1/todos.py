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


# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.core import database
# from app.api.v1.auth import get_current_user

# router = APIRouter()

# @router.get("/todos/")
# def get_todos(db: Session = Depends(database.get_db), current_user: dict = Depends(get_current_user)):
#     return read_todos(db, current_user["id"])

# @router.post("/todos/")
# def create_todo_endpoint(title: str, description: str = None, completed: bool = False, db: Session = Depends(database.get_db), current_user: dict = Depends(get_current_user)):
#     return create_todo(title, description, completed, db, current_user["id"])

# @router.put("/todos/{todo_id}")
# def update_todo_endpoint(todo_id: int, title: str = None, description: str = None, completed: bool = None, db: Session = Depends(database.get_db), current_user: dict = Depends(get_current_user)):
#     return update_todo(todo_id, title, description, completed, db, current_user["id"])

# @router.delete("/todos/{todo_id}")
# def delete_todo_endpoint(todo_id: int, db: Session = Depends(database.get_db), current_user: dict = Depends(get_current_user)):
#     return delete_todo(todo_id, db, current_user["id"])

# def read_todos(db: Session, user_id: int):
#     return db.query(database.Todo).filter(database.Todo.user_id == user_id).all()

# def create_todo(title: str, description: str, completed: bool, db: Session, user_id: int):
#     todo = database.Todo(
#         title=title,
#         description=description,
#         completed=completed,
#         user_id=user_id
#     )
#     db.add(todo)
#     db.commit()
#     db.refresh(todo)
#     return todo

# def update_todo(id: int, title: str, description: str, completed: bool, db: Session, user_id: int):
#     todo = db.query(database.Todo).filter(
#         database.Todo.id == id,
#         database.Todo.user_id == user_id
#     ).first()
#     if not todo:
#         raise HTTPException(status_code=404, detail="Todo not found")
    
#     if title is not None:
#         todo.title = title
#     if description is not None:
#         todo.description = description
#     if completed is not None:
#         todo.completed = completed
    
#     db.commit()
#     db.refresh(todo)
#     return todo

# def delete_todo(id: int, db: Session, user_id: int):
#     todo = db.query(database.Todo).filter(
#         database.Todo.id == id,
#         database.Todo.user_id == user_id
#     ).first()
#     if not todo:
#         raise HTTPException(status_code=404, detail="Todo not found")
    
#     db.delete(todo)
#     db.commit()
#     return {"message": "Todo deleted successfully"}

