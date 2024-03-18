#!/usr/bin/python3
"""Free from SQL Injection"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    state_name = sys.argv[4]

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE '%{}%'\
            ORDER BY id ASC".format(state_name)

    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
