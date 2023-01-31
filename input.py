from build import Database
from datetime import datetime

# class inhert from database build
#Class for insert students basic info into db
class Students(Database):
    def __init__(self):
        # use inhert from build
        self.exe = self.build_db()
        # initializing the methods
        self.student_info()
        self.student_check()
    def student_info(self):
        #define objects
        self.exe = self.cursor
        self.com = self.connect
        self.fetch = self.exe.fetchall()
        #define time&date objects
        now = datetime.now()
        self.dates = now.strftime("%d-%m-%Y")
        self.times = now.strftime("%H:%M:%S")
        #Input Student info
        print('Please fill the Student Info: ')
        self.name = str(input('Student Name: '))
        self.age = int(input('Student Age: '))
        self.addr = str(input('Student Address: '))
        self.Cls = str(input('Student Class: '))
        self.gender = str(input('Student Gender: '))
        #Insert students info into db
        self.exe.execute("INSERT INTO student(name,age,address,class,gender,time,date) VALUES (?,?,?,?,?,?,?)",
        (
        (self.name),
        (self.age),
        (self.addr),
        (self.Cls),
        (self.gender),
        (self.dates),
        (self.times)
        ))
    def student_check(self):
        self.exe.execute("SELECT name FROM student")
        for e in fetch:
            print(e)
        # self.com.commit()
        
    def query(self):
        self.exe.execute(f'SELECT * FROM student')
        self.fetch
        for x in self.fetch:
            print(x)
Students()