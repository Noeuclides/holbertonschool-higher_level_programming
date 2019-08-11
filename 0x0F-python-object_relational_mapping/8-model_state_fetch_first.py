#!/usr/bin/python3
"""
lists all State objects from database
"""
from sys import argv
import sqlalchemy as db
from sqlalchemy import (create_engine)
from model_state import Base, State

if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    connection = engine.connect()
    metadata = db.MetaData()
    states = db.Table('states', metadata, autoload=True, autoload_with=engine)
    sel = db.select([states])
    result = connection.execute(sel)
    resultset = result.fetchone()
    print("{}: {}".format(resultset[0], resultset[1]))
