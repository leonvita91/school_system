import sqlite3
import os
import colors

# build database
class Database():
    def __init__(self):
        #initialize the functions

        # Checking the existence of the database 
        self.check_db()
        self.build_db()
    def build_db(self):    
        self.connect = sqlite3.connect('School.db')
        self.cursor = self.connect.cursor()
        #Create first table
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS student(
            name text,
            address text,
            age integer,
            gender text,
            time blob,
            date blob
        )
        """)

        # Create second Table for score and class
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS point(
            class text,
            score integer
        )
        """)

        #Create Third Table for mat
        mat = []
        pick = str(input([]))
        self.cursor.execute(f""" CREATE TABLE IF NOT EXISTS point(
                {pick}    
                )
                """)


    #searching on database methods
    def check_db(self):
        self.path = []
        self.read = os.listdir('.')
        # looping around the current dir
        for i in self.read:
            if i == 'School.db':
                self.path.append(i)
        # checking if the database is exist or not
        if self.path == ['School.db']:
            print('database initialize....')
            return True
        if self.path != ['School.db']:
            print(colors.colors().red,"""   
            Database Not exist ??
            \nWarning if the database not exist it will:
            \nCreating new one However please check the backup folder
            \nIf you intend to restore the Database backup.
            \n----------------------------------------------
            """,colors.colors().end)
            return False
        
        # later should add backup functionillty ##################

Database()