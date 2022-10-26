from flask import Flask
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ARRAY, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from datetime import datetime, timedelta




app = Flask(__name__)
db = SQLAlchemy()

# TODO: connect to a local postgresql database
migrate = Migrate(app, db)



class Venue(db.Model):
  __tablename__='venuef'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  address = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  genres = db.Column(db.ARRAY(db.String), nullable=False)
  facebook_link = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
 
 

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
  website_link = db.Column(db.String(120))
  seeking_talent = db.Column(db.Boolean, default=False)
  seeking_description = db.Column(db.String(120))

  shows = db.relationship('Show', backref='venuef', lazy= False)

  def __repr__(self):
    return f'<Venue {self.id} {self.name}>'
#Venue is the parent (one-to-many) of a Show (Venue is also a foreign key)

class Artist(db.Model):
  __tablename__='artistf'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  phone = db.Column(db.String(120))
  genres = db.Column(db.ARRAY(db.String), nullable=False)
  facebook_link = db.Column(db.String(120))
  image_link = db.Column(db.String(500))
  
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
  website_link = db.Column(db.String(120))
  seeking_venue = db.Column(db.Boolean, default=False)
  seeking_description = db.Column(db.String(120))
  shows = db.relationship('Show', backref='artistf', lazy=False)
  
  def __repr__(self):
    return f'<Venue {self.id} {self.name}>'
#Artist is the parent (one-to-many) of a Show (Venue is also a foreign key)
  
  
  # TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.+++++
class Show(db.Model):
  __tablename__ = 'showf'
  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey('artistf.id', ondelete="CASCADE"), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('venuef.id', ondelete="CASCADE"), nullable=False)
  start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  
def __repr__(self):
    return f'<Show {self.id} {self.artist_id} {self.venue_id} {self.start_time}>'




