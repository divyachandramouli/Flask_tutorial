from flask import Flask
#Import SQL Alchemy
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
#Set a key value to the config string for your database
#mysql://username:password@server/db

# Connect the app with the database
app.config['SQLALCHEMY_DATABASE_URI']="postgres://postgres:cd123@localhost/flaskmovie"

# Create database object , pass app as arg
db=SQLAlchemy(app)

# Create database tables/schema
# A table for a user
class User(db.Model):
	id=db.Column(db.Integer, primary_key=True) #This will autoincrement for every user added
	username=db.Column(db.String(80), unique=True, nullable=False)
	email=db.Column(db.String(120), unique=True, nullable=False)

	def __init__(self,username,email):
		self.username=username
		self.email=email

	def __repr__(self):
		return '<User %r>' % self.username


@app.route('/')
def index():
	return "hello flask"


if __name__ == "__main__":
	app.run()