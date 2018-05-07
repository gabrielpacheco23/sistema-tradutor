from flask import render_template
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
	return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		print(form.username.data)
		print(form.password.data)
	else:
		print(form.errors)
	return render_template('login.html', form=form)


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})

def teste(info):
#	i = User("teste2", "teste", "Teste Teste", "teste2@teste.com")
#	db.session.add(i)
#	db.session.commit()
	r = User.query.filter_by(username="teste").all()
	print(r)
	return "Ok"
