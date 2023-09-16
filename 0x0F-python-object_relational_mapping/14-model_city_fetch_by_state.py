#!/usr/bin/python3

"""Module that lists all City objects from the database hbtn_0e_14_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    cities = session.query(City).order_by(City.id)
    for city in cities:
        for state in states:
            if city.state_id == state.id:
                print("{}: ({}) {}".format(state.name, city.id, city.name))
                break
    session.close()
