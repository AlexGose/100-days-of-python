from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

TMDB_API_KEY = os.getenv('TMDB_API_KEY')

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap(app)

db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(750))
    rating = db.Column(db.Float(), nullable=False)
    ranking = db.Column(db.Integer(), nullable=False)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()

all_movies = db.session.execute(db.select(Movie).order_by(Movie.year)).scalars().all()
if len(all_movies) == 0:  # add a movie for testing
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )
    db.session.add(new_movie)
    db.session.commit()


class RateMovieForm(FlaskForm):
    rating = StringField(label="Your Rating out of 10 (e.g., 7.5)", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField('Done')


class NewMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.year)).scalars().all()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['POST', 'GET'])
def edit():
    movie_id = request.args.get('id')
    movie = db.one_or_404(db.select(Movie).filter_by(id=movie_id))
    form = RateMovieForm()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie = db.one_or_404(db.select(Movie).filter_by(id=movie_id))
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = NewMovieForm()
    if form.validate_on_submit():
        return redirect(url_for('select', title=form.title.data))
    return render_template('add.html', form=form)


@app.route('/select')
def select():
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "query": request.args.get("title"),
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "include_adult": "false",
        "page": "1"
    }
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    movies = response.json()["results"]
    print(movies)
    return render_template('select.html', movies=movies)



if __name__ == '__main__':
    app.run(debug=True)
