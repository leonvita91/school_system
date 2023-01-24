import sqlite3
import os
import colors

#later should add backup functionillty
# build database
class Database():
    def __init__(self):
        #initialize the functions
        check = self.check_db()
        if check == True:
            print('database initialize....')
        elif check == False:
            print(colors.colors().red,"""Database Not exist ??
            \nWarning if the database not exist it will:
            Creating a new one >>>
            please Check the backup file.
            """,colors.colors().end)

        self.build_db()
    def build_db(self):    
        self.connect = sqlite3.connect('School.db')
        self.cursor = self.connect.cursor()
        #Create first table
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS student(
            name text,
            address text,
            age,
            gender,
            time,
            date
        )
        """)
        # Create second Table
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS status(
            materials,
            class,
            score
        )
        """)
    def check_db(self):
        self.path = []
        self.read = os.listdir('.')
        for i in self.read:
            if i == 'School.db':
                self.path.append(i)
        if self.path == ['School.db']:
            return True
        if self.path != ['School.db']:
            return False

Database()