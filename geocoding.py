import pandas as pd
import requests
import json
import geopy.distance
#####################################################################################################
data = pd.read_csv("stations.csv")

file_cities = "cit.txt"


cities = open(file_cities, "r") #input cities from db
cities_coords = open("cities_coords.txt", "a") #output cites + coords
next = cities.readline()
while next:
    parameter = {"key" : "EVL3umyRakXGnrfaVMmrL2evEScjo4uG", "location" : next}
    response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params = parameter)
    coords = json.loads(response.text)['results']

    lat = coords[0]['locations'][0]['latLng']['lat']
    lng = coords[0]['locations'][0]['latLng']['lng']
    print(next, lat, lng)
    cities_coords.write(next.rstrip('\n') + ', ' + str(lat) + ', ' + str(lng) + '\n')

    for i, row in data.iterrows():
        lat_station = data.at[i,'latitude']
        lng_station = data.at[i,'longitude']
        if geopy.distance.distance((lat,lng),(lat_station,lng_station)) <= 20:
            print ('Sighting ' + next.rstrip('\n') + ' in range of ' + data.at[i,'name'])

    next = cities.readline()
cities.close()
cities_coords.close()