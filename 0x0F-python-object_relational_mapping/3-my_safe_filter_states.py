#!/usr/bin/python3
"""
Script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument.
Safe from MySQL injections!
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
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s\
        ORDER BY states.id ASC", [state])
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
