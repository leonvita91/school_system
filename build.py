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
        self.add_sub()
    def build_db(self):    
        self.connect = sqlite3.connect('School.db')
        self.cursor = self.connect.cursor()
        #Create first table
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS student(
            student_id integer PRIMARY KEY AUTOINCREMENT,
            name text,
            age integer char(2),
            address text,
            class text,
            gender text,
            time blob,
            date blob
        )
        """)
        # Create second Table
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS point(
            score_id integer PRIMARY KEY AUTOINCREMENT,
            score integer
        )
        """)
        #Create 3th Table
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS mat(
            subject_id integer PRIMARY KEY AUTOINCREMENT,
            subjects text
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
        # Insert Subjects Into db
    
    def add_sub(self):
        print('Add Subject ?')
        user_dec = str(input('yes/no:\n'))
        if user_dec == 'yes' or 'y':
            self.sub_in = str(input('Subject Name: '))
            self.cursor.execute("INSERT INTO mat(subjects) VALUES (?)",
            (
            (self.sub_in)
            ))
            print("Would you like to add another Subject ? ")
            # ask user again
            self.try_again = str(input('yes/no: '))
            if self.try_again == 'y' or 'yes':
                self.add_sub()
            elif self.try_again == 'n' or 'no':
                pass
        elif user_dec == 'no' or 'n':
            pass

if __name__ == '__main__':
    Database()
        
# Note to insert new column into exist table 
# self.cursor.execute("""ALTER TABLE student ADD COLUMN ID interger """)