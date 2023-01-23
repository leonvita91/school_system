import sqlite3

# build database
build = sqlite3.connect('database.db')
connect = build.cursor()

# Create first table
connect.execute(""" CREATE TABLE IF NOT EXISTS student(
    name text,
    address text,
    age,
    gender,
    time,
    date
)
""")

# Create second Table
connect.execute(""" CREATE TABLE IF NOT EXISTS status(
    materials,
    class,
    score
)
""")
connect.execute('SELECT * FROM student ')
test = connect.fetchall()
print(test)