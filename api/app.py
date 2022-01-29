from datetime import datetime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:TAMUHACK@localhost/cloud-plant '
db = SQLAlchemy(app)
tempList = []

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Event: {self.description}"

    def __init__(self, description):
        self.description = description

@app.route('/api', methods={'GET'})
def index():
    return {
        'name': 'This is data from the backend'
    }

temperature = 70
@app.route('/temp', methods = ['GET', 'Post'])
def getTemp():
    if request.method == "GET":
        return {"temp": "{}f".format(temperature)}
    else:
        temperature = int(request.json['temperature'][:-1])
        print(temperature)
        return {
            "success": "temp changed to {}".format(temperature)
        }
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
    



if __name__ == '__main__':
    app.run()