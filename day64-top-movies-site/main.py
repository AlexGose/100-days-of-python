from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

TMDB_API_KEY = os.getenv('TMDB_API_KEY')
TMDB_API_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

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
    rating = db.Column(db.Float(), nullable=True)
    ranking = db.Column(db.Integer(), nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()

initial_movies = db.session.execute(db.select(Movie).order_by(Movie.year)).scalars().all()
if len(initial_movies) == 0:  # add a movie for testing if necessary
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, "
                    "pinned down by an extortionist's sniper rifle. Unable to leave "
                    "or receive outside help, Stuart's negotiation with the caller "
                    "leads to a jaw-dropping climax.",
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
        url = TMDB_API_URL + "/search/movie"
        params = {
            "query": form.title.data,
            "api_key": TMDB_API_KEY,
            "language": "en-US",
            "include_adult": "false",
            "page": "1"
        }
        response = requests.get(url=url, params=params)
        response.raise_for_status()
        movies = response.json()["results"]
        return render_template('select.html', movies=movies)
    return render_template('add.html', form=form)


@app.route('/select')
def select():
    movie_id = request.args.get('movie_id')
    if movie_id:
        url = TMDB_API_URL + f"/movie/{movie_id}"
        params = {
            'language': 'en-US',
            "api_key": TMDB_API_KEY,
        }
        response = requests.get(url=url, params=params)
        response.raise_for_status()
        movie_data = response.json()
        print(response.text)
        movie_to_add = Movie(
            title=movie_data['title'],
            year=int(movie_data['release_date'][:4]),
            description=movie_data['overview'],
            img_url=TMDB_IMAGE_URL + f"/{movie_data['poster_path']}"
        )
        db.session.add(movie_to_add)
        db.session.commit()
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
