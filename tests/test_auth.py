import pytest
from fastapi import status

def test_register_success(client):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@gmail.com",
            "username": "test",
            "first_name": "test",
            "last_name": "test",
            "password": "123"
        }
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "User created successfully"}

def test_login_success(client):
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
    
    # Try to login
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "test",
            "password": "123"
        }
    )
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()

def test_login_wrong_password(client):
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
    
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "test",
            "password": "wrong"
        }
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED 

