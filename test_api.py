import unittest
from api import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_authors(self):
        response = self.app.get('/authors')
        self.assertEqual(response.status_code, 200)

    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)

    def test_get_categories(self):
        response = self.app.get('/categories')
        self.assertEqual(response.status_code, 200)

    def test_get_books_by_author(self):
        author_id = 1
        response = self.app.get(f'/authors/{author_id}/books')
        self.assertEqual(response.status_code, 200)

    def test_get_books_by_category(self):
        category_id = 1
        response = self.app.get(f'/books/{category_id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()