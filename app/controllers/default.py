from flask import render_template, request, json
from app import app, db, socketio
from flask_socketio import SocketIO, send
from googletrans import Translator
#import pydeepl

#from app.models.tables import User
#from app.models.forms import LoginForm


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


translator = Translator()


@socketio.on('message')
def handle_messages(json):
    print('Receveid something' + str(json))
    if "data" not in json:
        translation = translator.translate(str(json['msg']), src='pt')
        print("Tradução:" + translation.text)
        json['transl'] = translation.text
    socketio.emit('response', json)
