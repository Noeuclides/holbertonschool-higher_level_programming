#!/usr/bin/python3
"""
links to the MySQL table
"""
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    class definition of a State
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))

    def __init__(self, id, name):
        self.id = id
        self.name = name
