from audioop import cross
from datetime import datetime
from types import coroutine
from flask import Flask, request
from flask import send_from_directory


from flask import copy_current_request_context
from flask_cors import CORS, cross_origin   

app = Flask(__name__, static_folder='/frontend/build', static_url_path='')

CORS(app)

@app.route('/api', methods={'GET'})
@cross_origin()
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

tempList={54:"234", 65:[657,23,65], "stuff":"lol"}


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


@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()