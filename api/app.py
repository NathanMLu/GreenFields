from datetime import datetime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:TAMUHACK@localhost/cloud-plant '
db = SQLAlchemy(app)

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

@app.route('/event', methods = ['POST'])
def create_event():
    description = request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    return format_event(event)

def format_event(event):
    return {
        "description": event.description,
        "id": event.id,
        "created_at": event.created_at,
    }

if __name__ == '__main__':
    app.run()