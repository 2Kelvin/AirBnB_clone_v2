#!/usr/bin/python3
"""Module contains Class DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

user = os.environ.get('HBNB_MYSQL_USER')
pswd = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
db = os.environ.get('HBNB_MYSQL_DB')
dbEnv = os.environ.get('HBNB_ENV')

appClasses = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}


class DBStorage():
    """Database storage class

    Attributes:
        __engine: SQLAlchemy engine
        __session: SQLAlchemy database session
    Methods:
        all(): Returns class instances
        new(): Adds instance to db session
        save(): save session changes to database
        delete(): deletes an object from the database
        reload(): creates a session
    """

    __engine = None
    __session = None

    def __init__(self):
        cnct = f'mysql+mysqldb://{user}:{pswd}@{host}/{db}'
        self.__engine = create_engine(cnct, pool_pre_ping=True)
        if dbEnv == 'test':
            Base.metadata.drop_all(bind=self.__engine, checkfirst=True)

    def all(self, cls=None):
        """Return all instances depending on the classname given

        Args:
            cls: class name argument
        """
        if not self.__session:
            self.reload()
        allObjs = {}
        if type(cls) == str:
            cls = appClasses.get(cls, None)
        if cls:
            for inst in self.__session.query(cls):
                allObjs[inst.__class__.__name__ + '.' + inst.id] = inst
        else:
            for cls in appClasses.values():
                for inst2 in self.__session.query(cls):
                    allObjs[inst2.__class__.__name__ + '.' + inst2.id] = inst2
        return allObjs

    def new(self, obj):
        """Add the instance to database

        Args:
            obj: instance to add to database
        """
        self.__session.add(obj)

    def save(self):
        """Commit changes to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from database if it exists

        Args:
            obj: object to delete from db
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Session creation"""
        Base.metadata.create_all(self.__engine)
        dbSession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(dbSession)

    def close(self):
        """Closing the DB session"""
        self.__session.remove()
