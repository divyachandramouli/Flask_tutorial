from flask import Flask
#Import SQL Alchemy
from flask_sqlalchemy import SQLAlchemy
#Import render template, request, redirect
from flask import render_template, request, redirect, url_for



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
	# Query db to retrieve users and display on homepage
	all_users=User.query.all() #Returns a list of objects (all users)
	#Pass the list of objects to the template using jinja

	# Filter data from db and display 
	oneItem = User.query.filter_by(username="test2").first() #Returns only one object even if there are multiple
	return render_template('add_user.html', all_users=all_users, oneItem = oneItem)

@app.route('/post_user',methods=['POST'])
def post_user():
	# Get the values submitted in the form and create a User class object to add
	user=User(request.form['username'], request.form['email'])
	# Add the object to the databse
	db.session.add(user)
	# Save it
	db.session.commit()
	return redirect(url_for('index'))#redirect to homepage

if __name__ == "__main__":
	app.debug=True
	app.run()