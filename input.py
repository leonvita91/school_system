import build as db
from datetime import datetime

#Time section

# In this section you will have options to Insert students info


class Students():
    def __init__(self):
        pass

    def student_info(self):
        now = datetime.now()
        self.dates = now.strftime("%d-%m-%Y")
        self.times = now.strftime("%H:%M:%S")
        print('Please fill the Student Info: ')
        self.name = str(input('Student Name: '))
        self.age = int(input('Student Age: '))
        self.addr = str(input('Student Address: '))
        self.gender = str(input('Student Gender: '))

    def student_field(self):
        self.materials = str(input(''))