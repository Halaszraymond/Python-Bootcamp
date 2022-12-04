import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

## API documentation: https://documenter.getpostman.com/view/24753526/2s8YzMXkLB

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random_cafe():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe={
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
        "has_sockets": random_cafe.has_sockets,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "id": random_cafe.id,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "map_url": random_cafe.map_url,
        "name": random_cafe.name,
        "seats": random_cafe.seats
    })


@app.route("/all", methods=["GET"])
def all_cafes():
    all_cafes = db.session.query(Cafe).all()
    cafe_list = []
    for cafe in all_cafes:
        a_cafe = {
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
            "has_sockets": cafe.has_sockets,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "id": cafe.id,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "map_url": cafe.map_url,
            "name": cafe.name,
            "seats": cafe.seats
        }
        cafe_list.append(a_cafe)
    return jsonify(cafes=cafe_list)


@app.route("/search", methods=["GET"])
def search_cafe():
    user_location_input = request.args.get("loc")
    the_cafe = db.session.query(Cafe).filter_by(location=user_location_input).first()
    if the_cafe:
        return jsonify(cafe={
            "can_take_calls": the_cafe.can_take_calls,
            "coffee_price": the_cafe.coffee_price,
            "has_sockets": the_cafe.has_sockets,
            "has_toilet": the_cafe.has_toilet,
            "has_wifi": the_cafe.has_wifi,
            "id": the_cafe.id,
            "img_url": the_cafe.img_url,
            "location": the_cafe.location,
            "map_url": the_cafe.map_url,
            "name": the_cafe.name,
            "seats": the_cafe.seats
        })
    else:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        })


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the new coffee price."})
    else:
        return jsonify(error={
            "Not Found": "Sorry, we couldnt update the coffee price"
        })


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    apikey = request.args.get("api-key")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe and apikey == "TopSecretAPIKey":
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe."})
    else:
        return jsonify(error={
            "Not Found": "Sorry, we couldnt delete the  cafe."
        })


if __name__ == '__main__':
    app.run(debug=True)
