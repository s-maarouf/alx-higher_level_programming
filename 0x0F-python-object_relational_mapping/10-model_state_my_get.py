#!/usr/bin/python3

"""Module that prints the state object with the name passed as argument"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == sys.argv[4]).first()
    if states:
        print("{}".format(states.id))
    else:
        print("Not found")
