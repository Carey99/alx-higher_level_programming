#!/usr/bin/python3
"""Lists all states with name string starting with N"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            port=3306
            )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
            ORDER BY states.id ASC")

    states = cursor.fetchall()

    for state_n in states:
        print(state_n)

    cursor.close()
    db.close()
