from flask import Flask
app = Flask(__name__)
''' Define the route
 Forward slash means root directory - this will be like the homepage
 We can call it index'''
@app.route('/') 
def index():
	return "<h1 style = 'color: blue'>Hello! Flask app successfully deployed on Heroku</h1>"
'''Can return just "hello flask" - this is html with inline styling

 If app.py is run directly from cmd line it's going to be assigned the value
  main, if it's assigned main, run the application'''

if __name__=="__main__":
	app.run()

'''If another script imports this app then it's not going to equal main
It will be the name of the script that is importing this
 This code is only for executing from the command line directly'''
