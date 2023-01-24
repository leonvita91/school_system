import build
import shutil
from datetime import datetime

now = datetime.now()
dates = now.strftime("%Y-%m-%d")
times = now.strftime("%H:%M:%S")
class Backup():
    def __init__(self):
        # initialize backup plan
        self.snap()
    def snap(self):
        self.show = build.Database
        self.result = self.show.check_db(self)
        if self.result == True:
            print('backing up database.....')
            shutil.copy('School.db','backup')
        if self.result == False:
            print('Sorry datebase not Exist !!')
            print("can't take backup now... please try to restored you backup ")

Backup()