#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from models.city import City
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """getter to list all cities"""
        cities = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                cities.append(city)
        return cities
