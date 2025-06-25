import json
import requests

def iss_position():

    req = requests.get("http://api.open-notify.org/iss-now.json")
    req_text=req.text
    req_dict = json.loads(req_text)
    iss_position=req_dict['iss_position']

    latitude = iss_position['latitude']
    longitude = iss_position['longitude']

    print(f"ISS Position: \n Longitude: {longitude} \n Latitude: {latitude} ")
    return
