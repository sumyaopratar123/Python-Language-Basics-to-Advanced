# Python Basics to Advanced Example
# Run: python sqlite_crud.py

import sqlite3

with sqlite3.connect(":memory:") as connection:
    connection.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT)")
    connection.execute("INSERT INTO students(name) VALUES (?)", ("Asha",))
    rows = connection.execute("SELECT id, name FROM students").fetchall()
    print(rows)
