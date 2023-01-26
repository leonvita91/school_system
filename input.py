from build import Database
from datetime import datetime

# class inhert from database build
class Students(Database):
    def __init__(self):
        # use inhert from build
        self.exe = self.build_db()
        # initializing
        self.student_info()
        self.query()
    def student_info(self):
        self.exe = self.cursor
        self.com = self.connect

        now = datetime.now()
        self.dates = now.strftime("%d-%m-%Y")
        self.times = now.strftime("%H:%M:%S")
        print('Please fill the Student Info: ')
        self.id = str(input('Student ID: '))
        self.name = str(input('Student Name: '))
        self.age = int(input('Student Age: '))
        self.addr = str(input('Student Address: '))
        self.gender = str(input('Student Gender: '))
        self.exe.execute("INSERT INTO student VALUES (?,?,?,?,?,?,?)",
        (
        (self.id),   
        (self.name),
        (self.age),
        (self.addr),
        (self.gender),
        (self.dates),
        (self.times)
        ))
        # commit into database
        self.com.commit()
        
    def query(self):
        self.exe.execute(f'SELECT rowid, * FROM student')
        fet = self.exe.fetchall()
        for x in fet:
            print(x)

Students()