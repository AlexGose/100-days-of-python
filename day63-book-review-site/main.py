from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    global all_books
    if request.method == 'POST':
        new_book = {
            'name': request.form['name'],
            'author': request.form['author'],
            'rating': request.form['rating']
        }
        all_books += [new_book]
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

