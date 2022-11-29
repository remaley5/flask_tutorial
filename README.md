# Full Stack Python Tutorial

## Setup

### Installation
1. Setup virtual environment
install: 
``` 
pip install pipenv
```
activate: 
```
pipenv shell
```
check the correct virtualenv:
``` 
cmd + shft + p
python: select interpreter
suggestions not match?
enter interpreter path: (e.g. /Users/sophiewillson/.local/share/virtualenvs/backend-GJngGTAQ)
```

2. Install Dependencies
All together: 
```
pipenv install flask flask-sqlalchemy psycopg2 python-dotenv flask-cors
```
Flask: (flask-sqlalchemy is an ORM that helps communicate with database like mongoose(mogodb))
```
pipenv install flask flask-sqlalchemy
```
Postgres:
```
psycopg2 python dotenv
```
Allow requests: Cors dependecy
```
flask-cors
```
note: packages should now all be in pip file

### Files
3. Create new File called app.py
Basic: 
```py
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


# Tells flask where app is running
app = Flask(__name__)

# Note: Not in the beginning of tutorial but had to add
# Note: SQLAlchemy no longer accepts the name 'postgres' it has to start with postgresql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/net'
db = SQLAlchemy(app)

app.route('/')
def hello():
    return 'Hey!'

if __name__ == '__main__':
    app.run()
```

4. Create file called .flaskenv
```
FLASK_APP=app
FLASK_ENV=development
```
Test running flask run - application should run on localhost