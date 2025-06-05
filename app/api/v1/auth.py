from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.auth import UserCreate, Token
from app.services.repositories.auth_repository import (
    register_user,
    authenticate_and_get_token
)

router = APIRouter(prefix="/auth")

@router.post("/register", response_model=dict)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return authenticate_and_get_token(db, form_data.username, form_data.password)