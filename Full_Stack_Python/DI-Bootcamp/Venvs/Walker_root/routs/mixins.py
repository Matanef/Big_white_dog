from django.conf import settings
import requests
import json

from Walker_root.routs.views import route


# handles Diresction requests from google
def Directions(*args, **kwargs):

    lat_a = kwargs.get("lat_a")
    long_a = kwargs.get("long_a")
    lat_b = kwargs.get("lat_b")
    long_b = kwargs.get("long_b")

    origins = f'{lat_a},{long_a}'
    destination = f'{lat_b},{long_b}'

    result = requests.get(
		'https://maps.googleapis.com/maps/api/directions/json?',
		 params={
		 'origin': origin,
		 'destination': destination,
		 "key": settings.GOOGLE_API_KEY
		 })
    
    directions = result.json()

# collecting information from the googlemaps API and store it in a variable


    if directions["status"] == "OK":

        route = directions["routes"][0]["legs"][0]
        origin = route["start_address"]
        destination = route["end_address"]
        distance = route["distance"]["text"]
        duration = route["duration"]["text"]

        overAllinstructions = [
            [
                s["distance"]["text"],
                s["duration"]["text"],
                s["html_instructions"],
            ]
            for s in route["overAllinstructions"]]
    
    return {
		    "origin": origin,
		    "destination": destination,
		    "distance": distance,
		    "duration": duration,
		    "steps": overAllinstructions
		}