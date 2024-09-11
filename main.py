from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Author(BaseModel):
    name: str
    bio: str

class Book(BaseModel):
    title: str
    author_id: int
    category_id: int

@app.get("/authors")
async def get_authors():
    return {"message": "List of authors"}

@app.get("/authors/{author_id}")
async def get_author(author_id: int):
    return {"message": "Details of author " + str(author_id)}

@app.get("/books")
async def get_books(author: int = None, category: int = None):
    if author:
        return {"message": "List of books written by " + str(author)}
    if category:
        return {"message": "List of books in category " + str(category)}
    return {"message": "List of books"}

@app.get("/categories")
async def get_categories():
    return {"message": "List of categories"}

@app.get("/categories/{category_id}/books")
async def get_books_by_category(category_id: int):
    return {"message": "List of books in category " + str(category_id)}

@app.get("/statistics/author_books")
async def author_books_statistics():
    return {"message": "Number of books per author"}

@app.get("/statistics/category_books")
async def category_books_statistics():
    return {"message": "Number of books per category"}