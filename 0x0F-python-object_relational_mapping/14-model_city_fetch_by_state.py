#!/usr/bin/python3
"""
Script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State, City).join(City).order_by(City.id).all()
    for state in states:
        print(f"{state[0].name}: ({state[1].id}) {state[1].name}")
