from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def connect():
    print('A client connected')

@socketio.on('message')
def message(data):
    print('Received message: {}'.format(data))
    send(data)

if __name__ == '__main__':
    socketio.run(app,allow_unsafe_werkzeug=True,)
