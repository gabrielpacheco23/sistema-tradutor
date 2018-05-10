from app import app, manager, socketio

if __name__ == "__main__":
	#manager.run()
	socketio.run(app)
