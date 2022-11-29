from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Tells flask where app is running
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/net_tutorial'
db = SQLAlchemy(app)
app.app_context().push()

# Create Model

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False) # type=string max characters = 100
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # imported above

    # String representation: 
    def __repr__(self): 
        return f"Event: {self.description}" # f string in python allows you to inject python variables # self.description refers to event itself

    # Set up constructor
    # Note: Because created_at has a default you don't need to add that into constructor
    def __init__(self, description): 
        self.description = description




@app.route('/')
def hello():
    return 'Hey!'

if __name__ == '__main__':
    app.run()