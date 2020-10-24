from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import hashlib

engine = create_engine('sqlite:///main.db', echo=True)
Base = declarative_base()


def calculate_digest(string):
    return hashlib.sha512(bytearray(string, 'utf-8')).hexdigest()


class User(Base):
    """"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = calculate_digest(password)


# create tables
Base.metadata.create_all(engine)
