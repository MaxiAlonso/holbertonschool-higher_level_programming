#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            port=3306,
            passwd=password,
            db=database)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
         INNER JOIN states ON states.id = cities.state_id\
             WHERE states.name = %s ORDER BY cities.id ASC", [state])
    rows = cur.fetchall()
    str = ""
    for row in rows:
        for col in row:
            str += (f"{col}, ")
    print(str[:-2])
    cur.close()
    db.close()
