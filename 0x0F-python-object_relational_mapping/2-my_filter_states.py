#!/usr/bin/python3

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
    cur.execute(f"SELECT * FROM states WHERE name LIKE '{state}'\
            ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
