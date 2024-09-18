from sqlalchemy import Column, String, Integer, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

book_category = Table('book_category', Base.metadata,
    Column('book_id', String, ForeignKey('books.ISBN')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'
    ISBN = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    publisher = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')
    categories = relationship('Category', secondary=book_category, back_populates='books')
    copies = relationship('Copy', back_populates='book')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    books = relationship('Book', secondary=book_category, back_populates='categories')

class Copy(Base):
    __tablename__ = 'copies'
    identifier = Column(String, primary_key=True)
    edition = Column(String)
    release_date = Column(Date)
    condition = Column(String)
    book_ISBN = Column(String, ForeignKey('books.ISBN'))
    book = relationship('Book', back_populates='copies')
