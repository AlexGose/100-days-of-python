from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)


db.create_all()

book = Book()
book.id = 1
book.title = 'Harry Potter'
book.author = 'J. K. Rowling'
book.rating = 9.3

db.session.add(book)
db.session.commit()

# import sqlite3
#
# db = sqlite3.connect('books-collection.db')
#
# cursor = db.cursor()
# create_table_sql = """
# CREATE TABLE books (
#     id INTEGER PRIMARY KEY,
#     title varchar(250) NOT NULL UNIQUE,
#     author varchar(250) NOT NULL,
#     rating FLOAT NOT NULL
# )
# """
# cursor.execute(create_table_sql)
#
# add_book_sql = """
# INSERT INTO books
#   VALUES (1, 'Tale of Two Cities', 'Charles Dickens', 9.3)
# """
#
# cursor.execute(add_book_sql)
# db.commit()
