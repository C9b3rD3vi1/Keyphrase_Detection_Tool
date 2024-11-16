
from flask import Flask, request, jsonify, request, render_template
import threading
from flask_socketio import SocketIO
import time



app = Flask(__name__)

socketio = SocketIO(app)

# log messages in memory
log_messages = []



# Endpoint to receive alerts from the client
@app.route('/alert', methods=['POST'])
def receive_alert():
    data = request.json
    if not data or 'keyword' not in data:
        return jsonify({"error": "Invalid data"}), 400

    keyword = data['keyword']
    print(f"Received alert for keyword: {keyword}")

    # Log the alert in memory
    log_messages.append(f"Keyword detected: {keyword} at {time.ctime()}")

     # Broadcast new log message to clients
    socketio.emit('new_log', {'message': log_messages[-1]})

    # Log the alert (could also save to a file or database)
    with open("server_logs.txt", "a") as log_file:
        log_file.write(f"Keyword detected: {keyword}\n")

    return jsonify({"message": "Alert received"}), 200


# Route to render the web dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html', logs=log_messages)

# Background task to periodically send logs
def send_logs():
    while True:
        socketio.sleep(5)  # Update every 5 seconds

# Start the background task
@app._got_first_request
def start_background_task():
    socketio.start_background_task(send_logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
