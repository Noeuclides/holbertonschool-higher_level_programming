#!/usr/bin/python3
"""
lists all State objects from database
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
    sel = s1.query(State).filter(State.name.op('regexp')(r'[a]')).all()
    for row in sel:
        print("{}: {}".format(row.id, row.name))
