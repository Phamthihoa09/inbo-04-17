from sqlalchemy.orm import sessionmaker
from .models import *

engine = create_engine('sqlite:///main.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin", "superstrongpass")
session.add(user)

# commit the record the database
session.commit()

