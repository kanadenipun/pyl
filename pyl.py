#!/usr/bin/python

from __future__ import print_function
from Adafruit_Thermal import *
import requests
import json

printer      = Adafruit_Thermal("/dev/ttyS0", 19200, timeout=5)

url = "https://api.mlab.com/api/1/databases/krpyl/collections/queue"
key = "?apiKey="

# insertData = json.loads('{"data":["sdcsd","dsdfsdfsd","fsdfsdf"]}')
# print("Data Inserted")
# insert = requests.post(url+key,json=insertData)
response = requests.get(url+key)
# print(response.content)


if response.status_code == 200 :
    data = json.loads(response.content)
    result = data[0]["data"]
    id = data[0]["_id"]["$oid"]

    for line in result:
        if(line == '$'):
            printer.feed(1)
        else:
            printer.println(line)

    response = requests.delete(url+"/"+id+key)
    #print("Deleted")
