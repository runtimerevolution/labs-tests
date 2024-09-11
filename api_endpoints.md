# API Endpoints

## Authors
- GET /authors 
    - Request: None
    - Response: List of all authors

- GET /authors/{author_id}
    - Request: Author ID
    - Response: Details of the author with the given ID

## Books
- GET /books
    - Request: None
    - Response: List of all books

- GET /books?author={author_id}
    - Request: Author ID
    - Response: List of books written by the author with the given ID

- GET /books?category={category_id}
    - Request: Category ID
    - Response: List of books in the given category

## Categories
- GET /categories
    - Request: None
    - Response: List of all categories

- GET /categories/{category_id}/books
    - Request: Category ID
    - Response: List of books in the given category

## Statistics
- GET /statistics/author_books
    - Request: None
    - Response: Number of books per author

- GET /statistics/category_books
    - Request: None
    - Response: Number of books per category