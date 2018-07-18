from flask import render_template, request, json
from flask import Flask, request, redirect, url_for, session, render_template, send_from_directory, flash
#from flask_login import login_user, logout_user
from app import app, db, socketio
from flask_socketio import SocketIO, send
from googletrans import Translator
#import pydeepl
#import pyaudio
#import speech_recognition as sr
#import unicodedata

from app.models.tables import User
from app.models import forms


####################### ROTAS ####################

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()
    if request.method == "POST":
        username = form.username.data,
        email = form.email.data,
        password = form.password.data
        nacionalidade = form.nacionalidade.data
        if username and email and password and nacionalidade:
            u = User(username, password, email, nacionalidade)
            db.session.add(u)
            db.session.commit()
            flash("Usuario registrado com sucesso", "success")
            return redirect(url_for('login'))
        else:
            flash("Falha no registro", "error")
    else:
        return render_template('register.html', form=form)

#@lm.user_loader
#def load_user(id):
#	return User.query.filter_by(id=id).first()

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Your email or password doesn't match!", "error")
    else:
        return render_template('login.html', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


################### MSG HANDLERS ##########################


translator = Translator()


@socketio.on('message')
def handle_messages(json):
    print('Receveid something' + str(json))
    if "data" not in json:
        translation = translator.translate(str(json['msg']), src='en', dest='pt')
        #translation = pydeepl.translate(str(json['msg']), 'ES')
        print("Tradução:" + translation.text)
        #print("Tradução: "+ translation)
        json['transl'] = translation.text
        #json['transl'] = translation
    socketio.emit('response', json)
