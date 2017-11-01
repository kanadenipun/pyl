from __future__ import print_function
import subprocess, time, socket
from Adafruit_Thermal import *
import psutil
import requests
import json

nextInterval = 0.0   # Time of next recurring operation
printer      = Adafruit_Thermal("/dev/ttyS0", 19200, timeout=5)

url = "https://api.mlab.com/api/1/databases/krpyl/collections/queue"
key = "?apiKey="

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8', 0))
	printer.print('My IP address is ' + s.getsockname()[0])
	printer.feed(3)
except:
	printer.boldOn()
	printer.println('Network is unreachable.')
	printer.boldOff()
	printer.print('Connect display and keyboard\n'
	  'for network troubleshooting.')
	printer.feed(3)
	exit(0)


def interval():
        p = subprocess.Popen(["python", "pyl.py"],
        stdout=subprocess.PIPE)

while(True) :

    t = time.time()
    
    if t > nextInterval:
        nextInterval = t + 5.0
        response = requests.get(url+key)
        data = json.loads(response.content)
        try:
                if(data[0]["data"]):  
                    result = interval()
                else:
                    print("blah")    
        except:
                print("Waiting...")
        
