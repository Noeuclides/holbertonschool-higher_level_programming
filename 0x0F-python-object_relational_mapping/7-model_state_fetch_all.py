#!/usr/bin/python3
"""
lists all State objects from database
"""
from sys import argv
import sqlalchemy as db
from model_state import Base, State

if __name__ == "__main__":
    
