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
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    s1 = session()
    new_state = State('California')
    new_city = City('San Francisco')
    new_city.state = new_state
    s1.add(new_state)
    s1.add(new_city)
    s1.commit()
    s1.close()
