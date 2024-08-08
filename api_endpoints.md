# API Endpoints

## Authors
- GET /api/authors
  Request: None
  Response: List of authors with authorId, name, and list of books

## Books
- GET /api/books
  Request: None
  Response: List of books with bookId, title, and list of categories

## Filter Books by Author
- GET /api/books/filterByAuthor/{authorId}
  Request: authorId
  Response: List of books by the specified author

## Filter Books by Category
- GET /api/books/filterByCategory/{categoryId}
  Request: categoryId
  Response: List of books in the specified category

## Basic Statistics
- GET /api/stats
  Request: None
  Response: Basic statistics like number of books per author and per category