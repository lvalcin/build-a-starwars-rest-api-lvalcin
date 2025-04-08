"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_user():
    User = User.query.all()
    # after 'in' is always the list you are looping through, it is being saved in the variable userData in this case
    user_list = [userData.serialize() for userData in User]
    return jsonify(user_list), 200

def get_character():
    Character = Character.query.all()
    character_list = [characterData.serialize() for characterData in Character]
    return jsonify(character_list), 200

def get_planet():
    Planet = Planet.query.all()
    planet_list = [planetData.serialize() for planetData in Planet]
    return jsonify(planet_list), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)


@app.route('/user', methods=['POST'])
def post_user():
    data = request.json
    new_user = User(
        # id = data["id"],
        email = data["email1"],
        password = data["password1"],
        is_active = data.get("is_active1")
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 200
# ,serialize converts the info into a json-type object