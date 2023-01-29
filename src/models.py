from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    surname = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (250))
    birth_year = db.Column(db.String (250))
    gender = db.Column(db.String (250))

    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }


class Planet(db.Model):
    
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (250))
    diameter = db.Column(db.String (250))
    rotation_period = db.Column(db.String (250))
    
    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Vehicle(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String (250))
    model = db.Column(db.String (250))
    vehicle_class = db.Column(db.String (250))

    def __repr__(self):
        return '<Vehicle %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):

    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    vehicle_id= db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #user = db.relationship(User)
    
    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id,
            "user_id": self.user_id,
           
            # do not serialize the password, its a security breach
        }
