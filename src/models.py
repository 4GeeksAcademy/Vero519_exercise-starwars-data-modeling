import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    birth_yearr = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    favorites = relationship('favorites', backref='character', lazy=True)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name_planet = Column(String(250))
    mass = Column(String(250))
    climate = Column(String(250), nullable=False)
    populate = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    favorites = relationship('favorites', backref='planets', lazy=True)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    email = Column(String(250))
    pasword = Column(String(250))

    favorites = relationship('favorites', backref='user', lazy=True)


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'),
        nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'),
        nullable=True)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
