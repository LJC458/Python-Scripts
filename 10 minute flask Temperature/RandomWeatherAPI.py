from flask import Flask
import random
from flask import jsonify

# A quick challenge to build an API using Flask that returns random JSON Weather data

weatherArray = ['Sun','Partial Cloud','Rain']

app = Flask(__name__)
@app.route('/api/')
def weather():
    condition = weatherArray[random.randrange(0,len(weatherArray)-1)]
    temp = random.randrange(20,25,1)
    weather = {'Temp':temp, 'Weather':condition}
    return jsonify(weather)

app.run()