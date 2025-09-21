import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "String Calculator API is running!"}

def test_calculate_basic():
    response = client.post("/calculate", json={"numbers": "1,2,3"})
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_calculate_empty_string():
    response = client.post("/calculate", json={"numbers": ""})
    assert response.status_code == 200
    assert response.json() == {"result": 0}

def test_calculate_invalid_input():
    """Test calculation with invalid input"""
    response = client.post("/calculate", json={"numbers": "1,abc,2"})
    assert response.status_code == 400
    assert "invalid literal for int()" in response.json()["detail"]
