import pandas as pd
import requests
import json
import geopy.distance
#####################################################################################################

file_cities = "data/cit.csv"
count = 1

cities = open(file_cities, "r") #input cities from db
cities_coords = open("data/cities_coords.csv", "a") #output cites + coords
cities_coords.write('city, state, lng, lat\n')
next = cities.readline()

while next:
    if count < 14950: #geocoding api erlaubt nur 15000 requests pro monat
        parameter = {"key" : "xkmKXYk7RidnvbHUHxAbHisL29iUDmXF", "location" : next}
    else:
        parameter = {"key" : "EVL3umyRakXGnrfaVMmrL2evEScjo4uG", "location" : next}

    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params = parameter)
    coords = json.loads(response.text)['results']
    count += 1

    # save lng lat
    lat = coords[0]['locations'][0]['latLng']['lat']
    lng = coords[0]['locations'][0]['latLng']['lng']
    print(next, lat, lng)
    cities_coords.write(next.rstrip('\n') + ', ' + str(lat) + ', ' + str(lng) + '\n')
    next = cities.readline()

cities.close()
cities_coords.close()