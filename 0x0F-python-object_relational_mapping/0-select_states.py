#!/usr/bin/python3
"""
 lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if len(argv) is not 4:
        pass

    db = MySQLdb.connect(
	    host='localhost',
	    user=argv[1],
	    passwd=argv[2],
	    db=argv[3]
	    )

    access = db.cursor()
    exec = access.execute("SELECT * FROM states")
    rows = access.fetchall()
    for row in rows:
	    print(row)
