from flask import Flask, render_template, request
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


@app.route('/form-entry', methods=['POST'])
def receive_data():
    print(request.form['name'])
    print(request.form['email'])
    print(request.form['phone'])
    print(request.form['message'])
    return f"<h1>Successfully sent your message</h1>"


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', blog=blogs_data[post_id-1])


if __name__ == '__main__':
    app.run(debug=True)
