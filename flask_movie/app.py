from flask import flask
#Import SQL Alchemy
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
#Set a key value to the config string for your database
#mysql://username:password@server/db

app.config['SQLALCHEMY_DATABASE_URI']="postgres://postgres:cd123@localhost/flaskmovie"

# Create database object , pass app as arg
db=SQLALchemy(app)

@app.route('/')
def index():
	return "hello flask"


if __name__ == "__main__"
	app.run()