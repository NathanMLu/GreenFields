from audioop import cross
from datetime import datetime
from types import coroutine
from flask import Flask, request
from flask import send_from_directory


from flask import copy_current_request_context
from flask_cors import CORS, cross_origin   

app = Flask(__name__, static_folder='frontend/build', static_url_path='')

CORS(app)

@app.route('/api', methods={'GET'})
@cross_origin()
def index():
    return {
        'name': 'This is data from the backend'
    }


temperature = 70
dampness = True
photoresister = False
score = 80

@app.route('/data', methods = ['GET', 'POST'])
def getData():
    global temperature
    global dampness
    global score
    if request.method == "GET":
        return {"temp" : "{}".format(temperature), "dampness": dampness, 'score': score}
    else:
        if ('temp' in request.json):
            temp = request.json['temp']
            if temp[-1]=='f' or temp[-1]=='c':
                temperature = int(temp[:-1])
            else:
                temperature = int(temp)
            print(temperature) 
            
        if ('dampness' in request.json):
            dampness =  bool(request.json['dampness'])
        if ('score' in request.json):
            score =  int(request.json['score'])
        return {"temp" : "{}".format(temperature), "dampness": dampness, 'score': score}


water = False
@app.route('/water', methods = ['POST', 'GET'])
def postWater():
    global water
    if request.method == 'POST':
        water = request.json["water"]
        print(water)
        return {"water": water}
    else:
        return  {"water": int(water)}

light = False
@app.route('/light', methods = ['POST', 'GET'])
def postLight():
    global light
    if request.methods == 'POST':
        light = request.json["lightSet"]
        print(light)
        return {"lightSet": light}
    else:
        return {"lightSet": light}


@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()