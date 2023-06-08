import sqlite3

db = sqlite3.connect('books-collection.db')

cursor = db.cursor()
create_table_sql = """
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title varchar(250) NOT NULL UNIQUE,
    author varchar(250) NOT NULL,
    rating FLOAT NOT NULL
)
"""
cursor.execute(create_table_sql)

add_book_sql = """
INSERT INTO books
  VALUES (1, 'Tale of Two Cities', 'Charles Dickens', 9.3)
"""

cursor.execute(add_book_sql)
db.commit()
