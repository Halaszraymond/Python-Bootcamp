from flask import request, Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
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
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    all_posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=all_posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = db.session.query(BlogPost).get(index)
    # for blog_post in posts:
    #     if blog_post["id"] == index:
    #         requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.session.query(BlogPost).get(post_id)
    edit = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit.validate_on_submit():
        post.title = edit.title.data
        post.subtitle = edit.subtitle.data
        post.author = edit.author.data
        post.img_url = edit.img_url.data
        post.body = edit.body.data
        db.session.commit()
        return redirect(url_for("show_post", index=post.id))
    return render_template("make-post.html", edit=True, form=edit)


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author.data,
            img_url=form.img_url.data,
            body=form.body.data,
            date=date.today().strftime("%B %d %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)

@app.route("/delete/<int:post_id>", methods=["GET", "POST"])
def delete_post(post_id):
    delete_a_post = db.session.query(BlogPost).get(post_id)
    db.session.delete(delete_a_post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
