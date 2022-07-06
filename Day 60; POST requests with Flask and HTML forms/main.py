from flask import Flask, render_template, request
import requests
from post import Post
import smtplib

OWN_EMAIL = "geenideejantje@yahoo.com"
OWN_PASSWORD = "ercuxucwgbhtvvmq"

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


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, message):
    email_message = f"Subject:NEW Message\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=OWN_EMAIL, password=OWN_PASSWORD)
        connection.sendmail(from_addr=OWN_EMAIL,
                            to_addrs=OWN_EMAIL,
                            msg=email_message)

@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in blog_content:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
