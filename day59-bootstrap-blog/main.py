from flask import Flask, render_template
import requests

response = requests.get('https://api.npoint.io/2a4be25f4f1d7f080ec5')
blogs_data = response.json()

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html', blogs_data=blogs_data)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
