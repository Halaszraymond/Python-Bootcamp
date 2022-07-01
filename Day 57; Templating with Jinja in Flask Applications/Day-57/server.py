from flask import Flask, render_template
import random
import requests
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.date.today().year
    my_name = "Raymond"
    return render_template("index.html", num=random_number, year=current_year, name=my_name)


@app.route('/guess/<name>')
def name_data(name):
    parameters = {
        "name": name,
    }
    gender_response = requests.get("https://api.genderize.io", params=parameters)
    age_response = requests.get("https://api.agify.io", params=parameters)
    gender_data = gender_response.json()
    age_data = age_response.json()
    guessed_name = name
    given_gender = gender_data["gender"]
    given_age = age_data["age"]
    return render_template("guess.html", name=guessed_name, gender=given_gender, age=given_age)


@app.route('/blog')
def get_blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", blogs=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
