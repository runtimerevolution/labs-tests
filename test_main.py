from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_authors():
    response = client.get("/authors")
    assert response.status_code == 200
    assert response.json() == {"message": "List of authors"}

def test_get_author():
    response = client.get("/authors/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Details of author 1"}

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == {"message": "List of books"}

def test_get_books_by_author():
    response = client.get("/books?author=1")
    assert response.status_code == 200
    assert response.json() == {"message": "List of books written by 1"}

def test_get_books_by_category():
    response = client.get("/books?category=1")
    assert response.status_code == 200
    assert response.json() == {"message": "List of books in category 1"}

def test_get_categories():
    response = client.get("/categories")
    assert response.status_code == 200
    assert response.json() == {"message": "List of categories"}

def test_get_books_by_category():
    response = client.get("/categories/1/books")
    assert response.status_code == 200
    assert response.json() == {"message": "List of books in category 1"}

def test_author_books_statistics():
    response = client.get("/statistics/author_books")
    assert response.status_code == 200
    assert response.json() == {"message": "Number of books per author"}

def test_category_books_statistics():
    response = client.get("/statistics/category_books")
    assert response.status_code == 200
    assert response.json() == {"message": "Number of books per category"}