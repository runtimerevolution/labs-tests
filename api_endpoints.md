# API Endpoints

## Authors

- GET /authors
  - Description: Get a list of all authors
  - Request: None
  - Response: List of authors with id, name, and date of birth

- GET /authors/{author_id}/books
  - Description: Get a list of books by a specific author
  - Request: author_id
  - Response: List of books with id, title, and isbn by the specified author

## Books

- GET /books
  - Description: Get a list of all books
  - Request: None
  - Response: List of books with id, title, and isbn

- GET /books/{category_id}
  - Description: Get a list of books by a specific category
  - Request: category_id
  - Response: List of books with id, title, and isbn in the specified category

## Categories

- GET /categories
  - Description: Get a list of all categories
  - Request: None
  - Response: List of categories with id and name