#!/usr/bin/python3
"""
links to the MySQL table
"""
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City

Base = declarative_base()


class State(Base):
    """
    class definition of a State
    """
    __tablename__ = 'states'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True)
    name = Column(String(128), nullable=False)
    state = relationship(City,
            backref=backref(
                'cities',
                uselist=True,
                cascade='delete,all'))

    def __init__(self, name):
        self.name = name
