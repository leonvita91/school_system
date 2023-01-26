import sqlite3
import backup_plan
import os
import colors

# build database
class Database():
    def __init__(self):
        #initialize the functions
        self.check_exist_db()
        self.build_db()
        self.checking_mat()
    def build_db(self):    
        self.connect = sqlite3.connect('School.db')
        self.cursor = self.connect.cursor()
        #Create first table
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS student(
            id integer NOT NULL PRIMARY KEY,
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
    #searching on Database if exist
    def check_exist_db(self):
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
            print(colors.colors().cyan,"""
            \nIF THIS YOUR FIRST START DON'T WORRY ABOUT THIS WARNING.....""",colors.colors().end,colors.colors().red,"""
            \nDatabase Not exist ??
            \nWarning if the database not exist it will:
            \nCreating A new one Automaticlly However please check the backup folder
            \nIf you intend to restore the Database backup.
            \n----------------------------------------------
            """,colors.colors().end)
            return False
#Create 3th Table
class materials(Database):
    def checking_mat(self):
        try:
            self.cursor.execute('SELECT * FROM mat')
        except:
            print(colors.colors().blue,
            'Nothing Still in Materials Table',
            colors.colors().end)
            self.insert_mat()
        ######## try to checking if the table is exist then drop the input mat
    def insert_mat(self):
        print('Would You Like To Add The New Materials?')
        user_dec = str(input('yes/no:\n'))
        if user_dec == 'yes' or 'y':
            print(colors.colors().pink,
            '\nYou Can ONLY ADD 9 Subjects Into Database',colors.colors().end)
            self.sub1 = str(input('1st subject: '))
            self.sub2 = str(input('2nd subject: '))
            self.sub3 = str(input('3rd subject: '))
            self.sub4 = str(input('4th subject: '))
            self.sub5 = str(input('5th subject: '))
            self.sub6 = str(input('6th subject: '))
            self.sub7 = str(input('7th subject: '))
            self.sub8 = str(input('8th subject: '))
            self.sub9 = str(input('9th subject: '))

            self.cursor.execute(f""" CREATE TABLE IF NOT EXISTS mat(
                {self.sub1} interger,
                {self.sub2} interger,
                {self.sub3} interger,
                {self.sub4} interger,
                {self.sub5} interger,
                {self.sub6} interger,
                {self.sub7} interger,
                {self.sub8} interger,
                {self.sub9} interger
                    )
                    """)
        elif user_dec == 'no' or 'n':
            pass
        else:
            print('Wrong input')
            self.insert_mat()


        
# Note to insert new column into exist table 
# self.cursor.execute("""ALTER TABLE student ADD COLUMN ID interger """)