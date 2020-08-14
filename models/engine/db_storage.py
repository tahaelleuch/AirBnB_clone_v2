#!/usr/bin/python3
"""moduleDBStorage"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {'User': User, 'Place': Place, 'State': State,
           'City': City, 'Amenity': Amenity, 'Review': Review}


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Inisialisation of class DBStorage"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB,
                                             pool_pre_ping=True))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """all"""
        new_dict = {}
        val_list = []
        if cls is not None:
            val_list = self.__session.query(cls).all()
        else:
            for cla_ss in classes:
                val_list += self.__session.query(classes[cla_ss]).all()
        for val in val_list:
            key = "{}.{}".format(val.__class__.__name__, val.id)
            new_dict[key] = val
        return (new_dict)

    def new(self, obj):
        """new"""
        self.__session.add(obj)

    def save(self):
        """save (commit the changes)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
