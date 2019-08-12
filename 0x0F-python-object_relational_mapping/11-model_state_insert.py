#!/usr/bin/python3
"""
adds the State object to database
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
    new_state = State('Louisiana')
    s1.add(new_state)
    s1.commit()
    print(new_state.id)
