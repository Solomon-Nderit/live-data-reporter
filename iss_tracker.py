import json
import requests
from datetime import datetime

def log_action(action, status):
    with open('logs.txt', 'a') as log:
        log.write(f"{datetime.now()} | {action} | {status}\n")

def iss_position():
    try:
        req = requests.get("http://api.open-notify.org/iss-now.json")
        req.raise_for_status()
        req_dict = req.json()
        iss_position = req_dict['iss_position']
        latitude = iss_position['latitude']
        longitude = iss_position['longitude']
        print(f"ISS Position: \n Longitude: {longitude} \n Latitude: {latitude} ")
        # Save to file
        with open('data/iss_data.txt', 'a') as f:
            f.write(f"{datetime.now()} | ISS Position | Longitude: {longitude}, Latitude: {latitude}\n")
        log_action('ISS Position', 'Success')
    except Exception as e:
        print('Error fetching ISS position:', e)
        log_action('ISS Position', f'Failed: {e}')
