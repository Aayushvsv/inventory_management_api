# In tests/test_main.py

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from inventory_api.main import app, get_db
from inventory_api.database import Base
import pytest

# Setup a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the database dependency to use the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create a Pytest fixture for the client
@pytest.fixture()
def client():
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)

# === YOUR TESTS START HERE ===

def test_create_product(client):
    # Test creating a new product
    response = client.post(
        "/products/",
        json={"name": "Test Product", "price": 10.0, "quantity": 100},
    )
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Test Product"
    assert "id" in data

def test_read_products(client):
    # First, create a product to ensure the database isn't empty
    client.post(
        "/products/",
        json={"name": "Another Test Product", "price": 20.0, "quantity": 50},
    )

    # Now, test reading all products
    response = client.get("/products/")
    data = response.json()

    assert response.status_code == 200
    assert len(data) > 0
    assert data[0]["name"] == "Another Test Product"