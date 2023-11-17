
import os
from pystyle import *
import time
import datetime
import requests
import psutil
import json

current_time = None

while True:
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    time.sleep(1)

print(Colorate.Horizontal(Colors.red_to_yellow, f"[{current_time} | Info]: All the imports have been initialize. (Information)"))
time.sleep(1.5)