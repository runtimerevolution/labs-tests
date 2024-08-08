# API Implementation

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/authors', methods=['GET'])
def get_authors():
    # Logic to get list of authors
    return jsonify({"authors": []})

@app.route('/authors/<author_id>/books', methods=['GET'])
def get_books_by_author(author_id):
    # Logic to get list of books by author_id
    return jsonify({"books": []})

@app.route('/books', methods=['GET'])
def get_books():
    # Logic to get list of books
    return jsonify({"books": []})

@app.route('/books/<category_id>', methods=['GET'])
def get_books_by_category(category_id):
    # Logic to get list of books by category_id
    return jsonify({"books": []})

@app.route('/categories', methods=['GET'])
def get_categories():
    # Logic to get list of categories
    return jsonify({"categories": []})