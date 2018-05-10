from flask import render_template, request, jsonify
from app import app, db, socketio
from flask_socketio import SocketIO, send

#from app.models.tables import User
#from app.models.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
	return render_template('index.html')

@socketio.on('message')
def handle_messages(json):
    print('Receveid something' + str(json))
    socketio.emit('response', json)
