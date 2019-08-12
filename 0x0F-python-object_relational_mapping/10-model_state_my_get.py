#!/usr/bin/python3
"""
prints the State object with the name passed as argument
"""
from sys import argv
import sqlalchemy as db
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    s1 = session()
    sel = s1.query(State).filter(State.name == argv[4]).all()
    if len(sel) == 0:
        print("Not found")
    else:
        print(sel[0].id)
