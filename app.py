from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__, template_folder='templates')
sm	= 0
ldr	= 0

#PostgreSQL DB config----------------------------------------------

# Backend Web-------------------------------------------------------
@app.route('/')
def home():
	return '<h2>Jaunty Jaugar</h2>'

@app.route('/sensor', methods = ['POST', 'GET'])
def sensor():
	global sm
	global ldr
	if request.method == 'POST':
		sm = request.form.get('sm')
		ldr = request.form.get('ldr')
#		return "{sm} {ldr}"
	return render_template('sensor.html', sm=sm, ldr=ldr)
		
#	else:
#		return "<h2>ERROR</h2>"

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)# Get port number of env at runtime, else use default port 5000
    app.run(host='0.0.0.0', port=port, debug=True)
