import build as db
import shutil
from datetime import datetime

now = datetime.now()
dates = now.strftime("%d-%m-%Y")
times = now.strftime("%H:%M:%S")

# Backup class & methods
class Backup():
    def __init__(self):
        # initialize backup plan
        self.snap()
    def snap(self):
        self.current_time = f"{dates} " + f"{times}" 
        self.show = db.Database
        self.result = self.show.check_db(self)
        if self.result == True:
            print('backing up database.....')
            shutil.copyfile('School.db', f'{self.current_time}')
            shutil.move(f'{self.current_time}','backup')
        if self.result == False:
            print('Sorry datebase not Exist !!')
            print("can't take backup now... please try to restored you backup ")

