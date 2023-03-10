import sqlite3
import backup_plan
import os
import colors

# build database
class Database():
    def __init__(self):
        #initialize methods
        self.check_exist_db()
        self.build_db()
        self.add_check_sub()
    def build_db(self):
        self.connect = sqlite3.connect('School.db')
        self.cursor = self.connect.cursor()
        #Create first table
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS student(
            student_id integer PRIMARY KEY AUTOINCREMENT,
            name text,
            age integer,
            address text,
            class text,
            gender text,
            time blob,
            date blob ) 
            """)
        # Create second Table
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS point(
            score_id integer PRIMARY KEY AUTOINCREMENT,
            score integer ) 
            """)
        #Create 3th Table
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS mat(
            subject_id integer PRIMARY KEY AUTOINCREMENT,
            subjects text ) 
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

    # Insert Subjects Into db
    def add_check_sub(self):
        print('Would you like to Add a Subject? ')
        user_dec = int(input('.> 1 yes:\n.> 2 no:\nAnswer: '))
        if user_dec == 1:
            self.sub_in = str(input('Subject Name: '))
            self.cursor.execute("SELECT subjects FROM mat")
            fet_check = self.cursor.fetchall()
            self.new_list = []
            for chk in fet_check:
                self.convert = ''.join(chk)
                self.new_list.append(self.convert)
            if self.sub_in in self.new_list:
                print(f'Subject {self.sub_in} is Already exsit !!')
                print("would you like to fetch the existin Subjects?\n>.1 yes\n>.2 no")
                user_check = int(input())
                if user_check == 1:
                    for x in fet_check:
                        print(x)
                elif user_check == 2:
                    pass

            elif self.sub_in not in self.new_list:
                self.cursor.execute("INSERT INTO mat(subjects) VALUES (?) ",
                ((self.sub_in),))
                self.connect.commit()
                print('new subject added')
            else:
                print('Wrong Input.')
        elif user_dec == 2:
            pass

if __name__ == '__main__':
    Database()
# Note to insert new column into exist table 
# self.cursor.execute("""ALTER TABLE student ADD COLUMN ID interger """)