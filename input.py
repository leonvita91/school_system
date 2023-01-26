from build import Database
from datetime import datetime

#Time section

# In this section you will have options to Insert students info


class Students(Database):
    def __init__(self):
        self.exe = self.build_db()
        self.student_info()
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
        self.com.commit()
        self.exe.execute('SELECT * FROM student')
        fet = self.exe.fetchall()
        for x in fet:
            print(x)

Students()