#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from os import getenv
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__="places"
        city_id = Column(String(60),ForeignKey("cities.id") ,nullable=False)
        user_id = Column(String(60),ForeignKey("users.id") , nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", backref="User", cascade="all, delete")
    else:
        
        @property
        def reviews(self):
            from models.review import Review
            """reviews filestorage"""
            f = []
            for i, j in models.storage.all(Review).items():
                if self.id == Review.place_id:
                    f.append(j)
            return f
