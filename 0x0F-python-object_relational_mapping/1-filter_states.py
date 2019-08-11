#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
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
            WHERE name REGEXP '^N'\
            COLLATE latin1_general_cs")
    rows = access.fetchall()
    for row in rows:
        print(row)
