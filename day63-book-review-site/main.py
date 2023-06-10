from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return f"<Book id:{self.id}, name:{self.name}, author:{self.author}, rating:{self.rating}>"


db.create_all()  # create database file and table


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.name)).scalars().all()
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(name=request.form['name'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'], )
def edit():
    book_id = request.args.get('id')
    book = db.one_or_404(db.select(Book).filter_by(id=book_id))
    if request.method == 'POST':
        book.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book)


@app.route('/delete')
def delete():
    book_id = request.args.get('id', '')
    if book_id != '':
        book = db.one_or_404(db.select(Book).filter_by(id=book_id))
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
