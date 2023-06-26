from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post", validators=[DataRequired()])


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.date.desc())).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = db.one_or_404(db.select(BlogPost).filter_by(id=index))
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=['GET', 'POST'])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=datetime.datetime.now().strftime('%B %d, %Y'),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form, type="New")


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    form = CreatePostForm()
    post_to_edit = db.one_or_404(db.select(BlogPost).filter_by(id=post_id))
    if request.method == 'GET':
        form.title.data = post_to_edit.title
        form.author.data = post_to_edit.author
        form.subtitle.data = post_to_edit.subtitle
        form.img_url.data = post_to_edit.img_url
        form.body.data = post_to_edit.body
        return render_template('make-post.html', form=form, type="Edit")
    if form.validate_on_submit():
        post_to_edit.title = form.title.data
        post_to_edit.author = form.author.data
        post_to_edit.subtitle = form.subtitle.data
        post_to_edit.img_url = form.img_url.data
        post_to_edit.body = form.body.data
        db.session.commit()
        return redirect(url_for('show_post', index=post_id))




@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)
