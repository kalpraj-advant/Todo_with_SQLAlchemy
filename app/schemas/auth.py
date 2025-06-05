from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str