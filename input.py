import build
from datetime import datetime
from time import sleep

now = datetime.now()
dates = now.strftime("%Y-%m-%d")
times = now.strftime("%H:%M:%S")

print(dates,times)