import pytest
from fastapi import status
from core.database import Todo

def test_get_todos_empty(client):
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@gmail.com",
            "username": "test",
            "first_name": "test",
            "last_name": "test",
            "password": "123"
        }
    )
    
    login_response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "test",
            "password": "123"
        }
    )
    token = login_response.json()["access_token"]
    
    response = client.get(
        "/api/v1/todos/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []

def test_get_todos_with_items(client, db):

    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@gmail.com",
            "username": "test",
            "first_name": "test",
            "last_name": "test",
            "password": "123"
        }
    )
    
    login_response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "test",
            "password": "123"
        }
    )
    token = login_response.json()["access_token"]
    
    test_todos = [
        Todo(title="Test Todo 1", description="Description 1", user_id=1),
        Todo(title="Test Todo 2", description="Description 2", user_id=1)
    ]
    for todo in test_todos:
        db.add(todo)
    db.commit()
    
    response = client.get(
        "/api/v1/todos/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    todos = response.json()
    assert len(todos) == 2
    assert todos[0]["title"] == "Test Todo 1"
    assert todos[1]["title"] == "Test Todo 2"

def test_get_todos_unauthorized(client):

    response = client.get("/api/v1/todos/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED 

def test_create_todo(client):
  
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@gmail.com",
            "username": "test",
            "first_name": "test",
            "last_name": "test",
            "password": "123"
        }
    )
    
    login_response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "test",
            "password": "123"
        }
    )
    token = login_response.json()["access_token"]
    
    response = client.post(
        "/api/v1/todos/?title=New Test Todo&description=This is a test todo",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    created_todo = response.json()
    assert created_todo["title"] == "New Test Todo"
    assert created_todo["description"] == "This is a test todo"
    assert "id" in created_todo

def test_update_todo(client, db):

    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@gmail.com",
            "username": "test",
            "first_name": "test",
            "last_name": "test",
            "password": "123"
        }
    )
    
    login_response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "test",
            "password": "123"
        }
    )
    token = login_response.json()["access_token"]
    
    test_todo = Todo(title="Original Todo", description="Original Description", user_id=1)
    db.add(test_todo)
    db.commit()
    db.refresh(test_todo)
    
    response = client.put(
        f"/api/v1/todos/{test_todo.id}?title=Updated Todo&description=Updated Description",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK
    updated_todo = response.json()
    assert updated_todo["title"] == "Updated Todo"
    assert updated_todo["description"] == "Updated Description"

def test_delete_todo(client, db):

    client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@gmail.com",
            "username": "test",
            "first_name": "test",
            "last_name": "test",
            "password": "123"
        }
    )
    
    login_response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "test",
            "password": "123"
        }
    )
    token = login_response.json()["access_token"]

    test_todo = Todo(title="Todo to Delete", description="This todo will be deleted", user_id=1)
    db.add(test_todo)
    db.commit()
    db.refresh(test_todo)
    
    response = client.delete(
        f"/api/v1/todos/{test_todo.id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == status.HTTP_200_OK

