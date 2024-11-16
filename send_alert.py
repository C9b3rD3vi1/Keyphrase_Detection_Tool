
import requests

SERVER_URL = "http://127.0.0.1:5000/alert"  # Replace with your server's URL

def send_alert_to_server(keyword):
    try:
        response = requests.post(SERVER_URL, json={"keyword": keyword})
        if response.status_code == 200:
            print(f"Alert sent for keyword: {keyword}")
        else:
            print(f"Failed to send alert: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending alert: {e}")
