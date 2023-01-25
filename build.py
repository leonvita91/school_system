import sqlite3
import os
import colors

# build database
class Database():
    def __init__(self):
        #initialize the functions
        self.check_db()
        self.build_db()
        self.checking_mat()
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


#Create Third Table for mat
class materials(Database):
    def checking_mat(self):
        self.cursor.execute('SELECT * FROM mat')
        fet = self.cursor.fetchall()
        ######## try to checking if the table is exist then drop the input mat
        # self.insert_mat()
        pass
    def insert_mat(self):
        print('Would you like to add Materials ?')
        user_dec = str(input('yes/no:\n'))
        if user_dec == 'yes':
            print(colors.colors().pink,
            '\nYou can add ONLY 9 Subjects into Database',colors.colors().end)
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
                {self.sub1} text,
                {self.sub2} text,
                {self.sub3} text,
                {self.sub4} text,
                {self.sub5} text,
                {self.sub6} text,
                {self.sub7} text,
                {self.sub8} text,
                {self.sub9} text
                    )
                    """)
        elif user_dec == 'no':
            pass
        else:
            print('Wrong input')
            self.insert_mat()
        
materials()