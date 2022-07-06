from flask import Flask, render_template
import requests
from post import Post

all_content = requests.get("https://api.npoint.io/6eb300bc8219c36fa9bb").json()
blog_content = []
for post in all_content:
    post_object = Post(post["id"], post["title"], post["subtitle"], post["body"])
    blog_content.append(post_object)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=blog_content)

@app.route('/about')
def go_to_about():
    return render_template("about.html")

@app.route('/contact')
def go_to_contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in blog_content:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)