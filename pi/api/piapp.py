from flask import Flask
import requests 

piapp = Flask(__name__)
@piapp.route('/')
def index():
    return {}

res = requests.post('http://localhost:5000/tests/endpoint', json={})
print ('response from server:',res.text)
if __name__ == '__main__':
    piapp.run()