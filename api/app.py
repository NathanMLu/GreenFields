from datetime import datetime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import gevent
from flask import copy_current_request_context

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:TAMUHACK@localhost/cloud-plant '
db = SQLAlchemy(app)

@app.route('/api', methods={'GET'})
def index():
    return {
        'name': 'This is data from the backend'
    }


temperature = 70
dampness = .5
photoresister = False
@app.route('/data', methods = ['GET', 'POST'])
def getData():
    global temperature
    global dampness
    if request.method == "GET":
        return {"temp" : "{}".format(temperature), "dampness": dampness}
    else:
        if (request.json['temp']):
            temp = request.json['temp']
            if temp[-1]=='f' or temp[-1]=='c':
                temperature = int(temp[:-1])
            else:
                temperature = int(temp)
            print(temperature) 
        if (request.json['dampness']):
            dampness =  request.json['dampness']

# temperature = 70
# @app.route('/temp', methods = ['GET', 'Post'])
# def getTemp():
#     if request.method == "GET":
#         return {"temp": "{}f".format(temperature)}
#     else:
#         temperature = int(request.json['temperature'][:-1])
#         print(temperature)
#         return {
#             "success": "temp changed to {}".format(temperature)
#         }

@app.route('/water', methods = ['POST'])
def postWater():
    water = request.json["water"]
    print(water)
    return {"water": water}

@app.route('/light', methods = ['POST'])
def postLight():
    light = request.json["lightSet"]
    print(light)
    return {"lightSet": light}

@app.route('/jsonexample', methods = ['POST'])
def jsonexample():
    data = request.get_json()
    temperature = data['temperature']
    moisture = data['moisture']


    



if __name__ == '__main__':
    app.run()