from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1 import todos

app = FastAPI(title="Todo API")

app.include_router(todos.router, prefix="/api/v1")

