#!/usr/bin/python3

"""Module that all State objects, and corresponding City objects,
                            from the database hbtn_0e_101_usa"""

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

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in cities:
            if city.state_id == state.id:
                print("    {}: {}".format(city.id, city.name))
