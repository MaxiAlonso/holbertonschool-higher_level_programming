#!/usr/bin/python3

import MySQLdb
from sys import argv

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
cur.execute("SELECT * FROM states WHERE name LIKE %s\
     ORDER BY states.id ASC", [state])
rows = cur.fetchall()
for row in rows:
    print(row)
