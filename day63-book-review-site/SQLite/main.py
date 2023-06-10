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

    def __repr__(self):
        return f"<Book id:{self.id}, title:{self.title}, author:{self.author}, rating:{self.rating}>"


db.create_all()  # create database file and table

# create a new record
book = Book(id=1, title='Harry Potter', author='J. K. Rowling', rating=9.3)

# Alternative:
# book = Book()
# book.id = 1
# book.title = 'Harry Potter'
# book.author = 'J. K. Rowling'
# book.rating = 9.3

db.session.add(book)
db.session.commit()

# read all records (bd.session.query is legacy)
all_books = db.session.execute(db.select(Book).order_by(Book.author)).scalars().all()
print(all_books)

# read a particular record
particular_book = db.first_or_404(db.select(Book).filter_by(title='Harry Potter'))
print(particular_book)

# update a particular record
particular_book.title = 'Harry Potter and the Chamber of Secrets'
db.session.commit()
print(particular_book)  # checked the database too

# update a record by primary key
book_id = 1
book_to_update = db.one_or_404(db.select(Book).filter_by(id=1))
book_to_update.title = 'Harry Potter and the Goblet of Fire'
db.session.commit()
print(book_to_update)

# delete a particular record by primary key
book_id = 1
book_to_delete = db.one_or_404(db.select(Book).filter_by(id=1))
db.session.delete(book_to_delete)
db.session.commit()  # checked the database too

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
