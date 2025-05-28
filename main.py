from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1 import todos, auth

app = FastAPI(title="Todo API")

app.include_router(todos.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Hello"}

