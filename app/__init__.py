from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_socketio import SocketIO


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

socketio = SocketIO(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


from app.models import tables, forms
from app.controllers import default
