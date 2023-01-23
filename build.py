import sqlite3

# The goal
# collect student info
# do add delete call insert
# orginesd the code to be more flexable

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
name = 'user'
add = 'aaa'
age = '234'
gender = 'asdfafd'
time = '32324'
date = '234324'
connect.execute("INSERT INTO student VALUES (?,?,?,?,?,?)",
(
(name),
(add),
(age),
(gender),
(time),
(date)
))
connect.execute('SELECT * FROM student ')
test = connect.fetchall()
print(test)