#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
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
    access.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s", (argv[4],))
    rows = access.fetchall()
    my_list = []
    for row in rows:
        my_list.append(row[0])
    print(', '.join(my_list))
	
