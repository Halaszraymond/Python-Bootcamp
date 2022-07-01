from flask import Flask, render_template
import requests
from post import Post

all_content = requests.get("https://api.npoint.io/4af156202f984d3464c3").json()
blog_content = []
for post in all_content:
    post_object = Post(post["id"], post["title"], post["subtitle"], post["body"])
    blog_content.append(post_object)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs=blog_content)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in blog_content:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
