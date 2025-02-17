from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO()

socketio.init_app(app, cors_allowed_origin = '*')
message_storage = []


@socketio.on('connect')
def handle_connect():
    print('Client Connected')

@socketio.on('disconnect')
def handle_connect():
    print('Client Disconnected')

@socketio.on('message')
def handle_message(message):
    global message_storage
    message_storage.append(message)
    print(f"Message: {message}")
    print("Message storage:", message_storage)
    socketio.emit('message', message)

@app.route("/")
def home():
    return render_template('base.html')

if __name__ == '__main__':

    app.debug = True
    socketio.run(app)

