from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def boldify():
        return "<b>" + function() + "</b>"
    return boldify


def make_emphasis(function):
    def emphasize():
        return "<em>" + function() + "</em>"
    return emphasize


def make_underlined(function):
    def underline():
        return "<u>" + function() + "</u>"
    return underline


@app.route('/')
def hello():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p>This is a paragraph</p1>' \
           '<hr>' \
           '<img src="https://media.giphy.com/media/aCqb9YW7QclN3rtto5/giphy-downsized-large.gif">'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'bye!'


@app.route('/username/<name>/<int:age>')
def age_greeting(name, age):
    return f"Hello {name}, your are {age} years old"


if __name__ == '__main__':
    app.run(debug=True)
