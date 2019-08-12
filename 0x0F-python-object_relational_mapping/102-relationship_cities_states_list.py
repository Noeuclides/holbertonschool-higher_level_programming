#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1],
                        sys.argv[2],
                        sys.argv[3]),
                        pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    s1 = session()
    result = s1.query(State).join(City).filter(State.id == City.state_id).all()
    for row in result:
        for city in row.cities:
            print("{}: {} -> {}".format(city.id, city.name, row.name))
