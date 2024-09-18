from flask import Flask, request, jsonify
from models import Author, Book, Category, Copy, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
DATABASE_URL = 'sqlite:///library.db'
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@app.route('/authors/', methods=['GET', 'POST'])
def manage_authors():
    session = Session()
    if request.method == 'POST':
        data = request.json
        author = Author(name=data['name'])
        session.add(author)
        session.commit()
        return jsonify({'id': author.id}), 201
    authors = session.query(Author).all()
    return jsonify([{'id': author.id, 'name': author.name} for author in authors])

@app.route('/books/', methods=['GET', 'POST'])
def manage_books():
    session = Session()
    if request.method == 'POST':
        data = request.json
        book = Book(
            ISBN=data['ISBN'],
            name=data['name'],
            description=data['description'],
            publisher=data['publisher'],
            author_id=data['author_id']
        )
        session.add(book)
        session.commit()
        return '', 201
    books = session.query(Book).all()
    return jsonify([{'ISBN': book.ISBN, 'name': book.name, 'description': book.description, 'publisher': book.publisher} for book in books])

@app.route('/categories/', methods=['GET', 'POST'])
def manage_categories():
    session = Session()
    if request.method == 'POST':
        data = request.json
        category = Category(name=data['name'])
        session.add(category)
        session.commit()
        return jsonify({'id': category.id}), 201
    categories = session.query(Category).all()
    return jsonify([{'id': category.id, 'name': category.name} for category in categories])

@app.route('/copies/', methods=['GET', 'POST'])
def manage_copies():
    session = Session()
    if request.method == 'POST':
        data = request.json
        copy = Copy(
            identifier=data['identifier'],
            edition=data['edition'],
            release_date=data['release_date'],
            condition=data['condition'],
            book_ISBN=data['book_ISBN']
        )
        session.add(copy)
        session.commit()
        return '', 201
    copies = session.query(Copy).all()
    return jsonify([{'identifier': copy.identifier, 'edition': copy.edition, 'release_date': copy.release_date, 'condition': copy.condition} for copy in copies])

if __name__ == '__main__':
    app.run()
