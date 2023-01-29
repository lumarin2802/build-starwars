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
from models import db, User, Character, Planet, Vehicle, Favorites
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


#aqui comienzo los endpoints
@app.route('/user', methods=['GET'])
def handle_hello():
    #con estas dos lineas de codigo consultamos todos los datos de una tabla
    allusers = User.query.all()
    #print(allusers)
    results = list(map(lambda item: item.serialize(),allusers))
    #print(results)
    # response_body = {
    #     "msg": "Hello, this is your GET /user response "
    # }
    return jsonify(results), 200

#obteniendo info de un solo usuario
@app.route('/user/<int:user_id>', methods=['GET'])
def get_info_user(user_id):
    print(user_id)
    # Para hacer una consulta a la tabla por alguien especifico.Aca estamos llamando a la tabla user, apuntamos a la propiedad query para decir que vamos a hacer una consulta, utiliza el metodo filter_by y le vas a pasar los valores de la propiedad que quieres consultar y el valor que quieres consultar, y al final le colocamos el metodo .first()
    #peter = User.query.filter_by(username='peter').first()
    user = User.query.filter_by(id=user_id).first()
    #print(user.serialize())
    return jsonify(user.serialize()), 200

@app.route('/planet', methods=['GET'])
def info_planets():
    #con estas dos lineas de codigo consultamos todos los datos de una tabla
    allplanet = Planet.query.all()
    #print(allplanets)
    results_planet = list(map(lambda item: item.serialize(),allplanet))
    #print(results_planet)
    
    return jsonify(results_planet), 200

    #obteniendo info de un solo planeta
@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_info_planet(planet_id):
    #print(planet_id)
    planet = Planet.query.filter_by(id=planet_id).first()
    #print(planet.serialize())
    return jsonify(planet.serialize()), 200

@app.route('/vehicle', methods=['GET'])
def info_vehicles():
    #con estas dos lineas de codigo consultamos todos los datos de una tabla
    allvehicle = Vehicle.query.all()
    #print(allvehicle)
    results_vehicle = list(map(lambda item: item.serialize(),allvehicle))
    #print(results_vehicle)
    return jsonify(results_vehicle), 200

    #obteniendo info de un solo vehiculo

@app.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def get_info_vehicle(vehicle_id):
    #print(vehicle_id)
    vehicle = Vehicle.query.filter_by(id=vehicle_id).first()
    print(vehicle.serialize())
    return jsonify(vehicle.serialize()), 200

@app.route('/character', methods=['GET'])
def info_characters():
    #con estas dos lineas de codigo consultamos todos los datos de una tabla
    allcharacter = Character.query.all()
    #print(allcharacter)
    results_character = list(map(lambda item: item.serialize(),allcharacter))
    #print(results_character)
    return jsonify(results_character), 200    

#obteniendo info de un solo character

@app.route('/character/<int:character_id>', methods=['GET'])
def get_info_character(character_id):
    #print(character_id)
    character = Character.query.filter_by(id=character_id).first()
    print(character.serialize())
    return jsonify(character.serialize()), 200

    
#terminan los endpoints

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
