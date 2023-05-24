from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


def guess_gender(name):
    response = requests.get(f"https://api.genderize.io/?name={name}")
    return response.json()['gender']


def guess_age(name):
    response = requests.get(f"https://api.agify.io/?name={name}")
    return response.json()['age']


@app.route('/')
def home():
    random_number = random.randint(0, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number,
                           current_year=current_year)


@app.route('/guess/<name>')
def guess(name):
    return render_template('guess.html', name=name, gender=guess_gender(name),
                           age=guess_age(name))


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
