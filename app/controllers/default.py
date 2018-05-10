from flask import render_template, request, jsonify
from app import app, db, socketio
from flask_socketio import SocketIO, send

from app.models.tables import User
from app.models.forms import LoginForm


@app.route("/index", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
	return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
	print('Message: '+msg)
	send(msg, broadcast=True)

#@app.route("/login", methods=["GET","POST"])
#def login():
#	form = LoginForm()
#	if form.validate_on_submit():
#		print(form.username.data)
#		print(form.password.data)
#	else:
#		print(form.errors)
#	return render_template('login.html', form=form)
