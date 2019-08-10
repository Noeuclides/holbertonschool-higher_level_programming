#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
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
