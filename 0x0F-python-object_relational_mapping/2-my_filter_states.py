#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    access = db.cursor()
    access.execute("SELECT * FROM states\
            WHERE states.name = '{}'".format(argv[4]))
    rows = access.fetchall()
    for row in rows:
        print(row)
