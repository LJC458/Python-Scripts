

import requests
import json
import datetime 
import time

# A quick challenge to build an API using Flask that returns random JSON Weather data
# This file gets the JSON From the API and writes it to a file after parsing

def GetWeather():


    while True:
        response = requests.get('http://localhost:5000/api/')
        Data=json.loads(response.text)

        times = time.strftime("%b %d %Y %H:%M:%S", time.localtime())

        f = open(".\weatherlog.txt", "a")
        f.write("time: " +times + ' Temp: ' +str(Data["Temp"]) + ' Weather ' +Data["Weather"] + "\n")
        f.close()
        
GetWeather()


