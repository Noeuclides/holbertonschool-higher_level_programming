#!/usr/bin/python3
"""
City objects from database
"""
from sys import argv
import sqlalchemy as db
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    s1 = session()
    sel = s1.query(City, State).filter(State.id == City.state_id)
    for row in sel:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))
    s1.close()
