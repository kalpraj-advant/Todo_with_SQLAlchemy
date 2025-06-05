from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None