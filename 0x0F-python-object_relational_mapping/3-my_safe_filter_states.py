#!/usr/bin/python3
"""
safe from MySQL injections
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
	    host='localhost',
	    user=argv[1],
	    passwd=argv[2],
	    db=argv[3]
	    )

    access = db.cursor()
    exec = access.execute("SELECT * FROM states WHERE states.name = '{}'".format(argv[4]))
    rows = access.fetchall()
    for row in rows:
	    print(row)
