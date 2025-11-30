from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@socketio.on("send_message")
def handle_message(data):
    # Broadcast to all clients
    emit("new_message", data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
