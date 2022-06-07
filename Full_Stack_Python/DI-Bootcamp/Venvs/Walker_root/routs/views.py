from django.shortcuts import render
from django.conf import settings
import googlemaps
import requests
import json
import pprint
import time
from .mixins import Directions

'''
Basic view for routing
'''

def route(request):
    context = {"google_api_key": settings.GOOGLE_API_KEY}
    return render(request, 'routs/route.html', context)

'''
Basic view for displaying a map

the lat and long are here to receive information from the places we requested
'''

def map (request):
    lat_a = request.GET.get("lat_a")
    long_a = request.GET.get("long_a")
    lat_b = request.GET.get("lat_b")
    long_b = request.GET.get("long_b")
    directions = Directions(
        lat_a= lat_a,
        long_a= long_a,
        lat_b= lat_b,
        long_b=long_b,
        )

    context = {
    "google_api_key": settings.GOOGLE_API_KEY,
	"lat_a": lat_a,
	"long_a": long_a,
	"lat_b": lat_b,
	"long_b": long_b,
	"origin": f'{lat_a}, {long_a}',
	"destination": f'{lat_b}, {long_b}',
	"directions": directions,
    }
    return render(request, 'routs/map.html', context)