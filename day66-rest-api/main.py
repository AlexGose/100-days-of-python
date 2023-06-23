import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

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

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/random")
def random_cafe():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars().all()
    cafe = random.choice(all_cafes)
    return jsonify(cafe=cafe.to_dict())


@app.route('/all')
def get_cafes():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route('/search')
def search():
    location = request.args.get('loc')
    cafe_at_location = db.session.execute(db.select(Cafe).filter_by(location=location)).scalars().first()
    if cafe_at_location:
        return jsonify(cafe=cafe_at_location.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


def str2bool(s):
    """
    Returns boolean for input string `"True"` or `"False"`
    """
    if s == "True" or s == "true":
        return True
    elif s == "False" or s == "false":
        return False
    else:
        raise ValueError("Input string must be 'True' or 'False'")


@app.route('/add', methods=['POST'])
def add():
    new_cafe = Cafe(
        name=request.form['name'],
        map_url=request.form['map_url'],
        img_url=request.form['img_url'],
        location=request.form['location'],
        seats=request.form['seats'],
        has_toilet=str2bool(request.form['has_toilet']),
        has_wifi=str2bool(request.form['has_wifi']),
        has_sockets=str2bool(request.form['has_sockets']),
        can_take_calls=str2bool(request.form['can_take_calls']),
        coffee_price=request.form['coffee_price'],
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update(cafe_id):
    new_price = request.args.get('new_price')
    cafe_to_update = db.session.execute(db.select(Cafe).filter_by(id=cafe_id)).scalars().first()
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Successfully updated the price.")
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    api_key = request.args.get('api-key')
    if api_key != 'TopSecretAPIKey':
        return jsonify(error="Sorry, that's not allowed.  Make sure you have the correct API key."), 403
    cafe_to_delete = db.session.execute(db.select(Cafe).filter_by(id=cafe_id)).scalars().first()
    if cafe_to_delete:
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(success="Successfully deleted the cafe.")
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404


if __name__ == '__main__':
    app.run(debug=True)
