from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import hashlib

engine = create_engine('sqlite:///auth/users.db', echo=True)
Base = declarative_base()


def calculate_digest(string):
    return hashlib.sha512(bytearray(string, 'utf-8')).hexdigest()


class User(Base):
    """"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    last_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    password = Column(String)

    def __init__(self,
                 username,
                 password,
                 first_name=None,
                 last_name=None,
                 middle_name=None,
                 ):
        """"""
        self.username = username
        self.password = calculate_digest(password)
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name


# create tables
Base.metadata.create_all(engine)
