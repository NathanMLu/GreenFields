from flask import Flask
import requests 

piapp = Flask(__name__)
@piapp.route('/')
def index():
    return {}
temp = 74
damp = False
score = 73
res = requests.post('https://aqueous-tor-90407.herokuapp.com/data', json={'data'})
print ('response from server:',res.text)
if __name__ == '__main__':
    piapp.run()