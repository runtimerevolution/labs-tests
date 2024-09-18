
# labs-tests

## Database Model

```mermaid
erDiagram
    AUTHOR ||--o{ BOOK: writes
    BOOK ||--o{ CATEGORY: falls_in
    BOOK ||--o{ COPY: has_instances

    AUTHOR {
        int id
        string name
    }

    BOOK {
        string ISBN
        string name
        string description
        string publisher
        int author_id
    }

    CATEGORY {
        int id
        string name
    }

    COPY {
        string identifier
        string edition
        date release_date
        string condition
        string book_ISBN
    }
```

## API Endpoints

### Authors
- **GET /authors/**: Get list of authors
- **POST /authors/**: Create a new author

### Books
- **GET /books/**: Get list of books
- **POST /books/**: Create a new book

### Categories
- **GET /categories/**: Get list of categories
- **POST /categories/**: Create a new category

### Copies
- **GET /copies/**: Get list of copies
- **POST /copies/**: Create a new copy

