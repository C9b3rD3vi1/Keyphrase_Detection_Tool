
from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to receive alerts
@app.route('/alert', methods=['POST'])
def receive_alert():
    data = request.json
    if not data or 'keyword' not in data:
        return jsonify({"error": "Invalid data"}), 400

    keyword = data['keyword']
    print(f"Received alert for keyword: {keyword}")

    # Log the alert (could also save to a file or database)
    with open("server_logs.txt", "a") as log_file:
        log_file.write(f"Keyword detected: {keyword}\n")

    return jsonify({"message": "Alert received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)