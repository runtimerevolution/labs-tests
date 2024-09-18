
import requests

BASE_URL = 'http://localhost:5000'

class TestCopies:

    def test_create_copy(self):
        response = requests.post(f'{BASE_URL}/copies/', json={
            'identifier': 'copy1',
            'edition': 'First Edition',
            'release_date': '2021-01-01',
            'condition': 'New',
            'book_ISBN': '1234567890'
        })
        assert response.status_code == 201

    def test_get_copies_list(self):
        response = requests.get(f'{BASE_URL}/copies/')
        assert response.status_code == 200

    def test_get_copies_list_empty(self):
        response = requests.get(f'{BASE_URL}/copies/')
        assert response.json() == []

    def test_get_copy_with_id(self):
        response = requests.get(f'{BASE_URL}/copies/copy1/')
        assert response.status_code == 200
