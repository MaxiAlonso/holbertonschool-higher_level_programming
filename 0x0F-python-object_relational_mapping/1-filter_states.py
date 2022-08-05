#!/usr/bin/python3

import MySQLdb
from sys import argv

username = argv[1]
password = argv[2]
database = argv[3]
db = MySQLdb.connect(
        host="localhost",
        user=username,
        port=3306,
        passwd=password,
        db=database)

cur = db.cursor()
cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%'")
rows = cur.fetchall()
for row in rows:
    print(row)
