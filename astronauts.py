import json
import requests



def people_in_space():
    req = requests.get("http://api.open-notify.org/astros.json")
    req_text=req.text
    req_dict = json.loads(req_text)

    with open('astronaut_names.txt', 'w') as f:
        for person in req_dict['people']:
            f.write(person['name'] + '\n')
    return

