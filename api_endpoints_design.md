# API Endpoints Design
## Authors
- GET /authors
  - Request: None
  - Response: List of Authors
- POST /authors
  - Request: Author details
  - Response: Created Author
## Books
- GET /books
  - Request: None
  - Response: List of Books
- GET /books?author={author_id}
  - Request: Author ID
  - Response: List of Books by Author
- GET /books?category={category_id}
  - Request: Category ID
  - Response: List of Books by Category
- POST /books
  - Request: Book details
  - Response: Created Book
## Categories
- GET /categories
  - Request: None
  - Response: List of Categories
- POST /categories
  - Request: Category details
  - Response: Created Category