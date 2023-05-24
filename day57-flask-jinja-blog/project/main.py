from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<num>')
def get_post(num):
    return render_template("post.html", post=all_posts[int(num)-1], num=num)


if __name__ == "__main__":
    app.run(debug=True)
