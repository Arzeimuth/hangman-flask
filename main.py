from flask import Flask, render_template, make_response, redirect
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins=['http://localhost:3000','https://nabify.com','https://www.nabify.com'])

# @app.route('/')
# def index():
#     return render_template('index.html')

@socketio.on("connect")
def printConnect():
    print("CONNECTED")

@socketio.on("message")
def handleMessage(data):
    emit("new_message",data,broadcast=True)
    
if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=5004)