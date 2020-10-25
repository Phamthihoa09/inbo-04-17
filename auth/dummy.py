from sqlalchemy.orm import sessionmaker
from models import *

# This file is only needed to create "test user"

engine = create_engine('sqlite:///auth/users.db', echo=True)
Base.metadata.bind = engine

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin", "superstrongpass", 'Victor', 'Nguen')
session.add(user)

# commit the record the database
session.commit()

