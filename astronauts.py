import json
import requests
from datetime import datetime



def log_action(action, status):
    with open('logs.txt', 'a') as log:
        log.write(f"{datetime.now()} | {action} | {status}\n")

def people_in_space():
    try:
        req = requests.get("http://api.open-notify.org/astros.json")
        req.raise_for_status()
        req_dict = req.json()
        people = req_dict.get('people', [])
        if not people:
            print('No astronaut data found.')
            log_action('Fetch Astronauts', 'Failed: No data')
            return
        print('\nAstronauts in space:')
        with open('data/iss_data.txt', 'a') as f:
            f.write(f"{datetime.now()} | Astronauts in Space:\n")
            for person in people:
                name = person.get('name', 'Unknown')
                craft = person.get('craft', 'Unknown')
                print(f"- {name} ({craft})")
                f.write(f"- {name} ({craft})\n")
            f.write('\n')
        log_action('Fetch Astronauts', 'Success')
    except Exception as e:
        print('Error fetching astronaut data:', e)
        log_action('Fetch Astronauts', f'Failed: {e}')

