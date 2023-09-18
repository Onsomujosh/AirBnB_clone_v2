#!/usr/bin/python3
'''database storage engine'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity

classes = {"Amenity": Amenity, "City": City, "Place": Place,
            "Review": Review, "State": State, "User": User}


class DBStorage:
    '''database storage engine for mysql storage'''
    __engine = None
    __session = None

    def __init__(self):
        '''instantiate new dbstorage'''
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    HBNB_MYSQL_USER,
                    HBNB_MYSQL_PWD,
                    HBNB_MYSQL_HOST,
                    HBNB_MYSQL_DB
                    ), pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, clss=None):
        '''return a dictionary, key and value from the current db session
        '''
        dictionary = {}
        if clss in None:
            for c in classes.values():
                objcts = self.__session.query(c).all()
                for objct in objcts:
                    key = objct.__class__.__name__ + '.' + objct.id
                    dictionary[key] = objct
        else:
            objcts = self.__session.query(clss).all()
            for objct in objcts:
                key = objct.__class__.__name__ + '.' + objct.id
                dictionary[key] = objct
        return dictionary

    def new(self, objct):
        '''objct is added to the current session in the db'''
        if objct is not None:
            try:
                self.__session.add(objct)
                self.__session.flush()
                self.__session.refresh(objct)
            except Exception as exc:
                self.__session.rollback()
                raise exc

    def save(self):
        '''deletes the objct from the current db session if not None'''
        if objct is not None:
            self.__session.query(type(objct)).filter(
                type(objct).id == objct.id).delete()

    def reload(self):
        '''refreshes the db'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                            expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """ends the working sqlalchemy session"""
        self.__session.close()
