import geopy.distance
import pandas as pd

stationInfo = pd.read_csv("stations_us.csv")
sightingInfo = pd.read_csv("cities_coords.csv")
range = open("inRange_new.txt", "a")
count = 0

for a, rows in sightingInfo.iterrows():
    sighting_lat = sightingInfo.at[a,'lat']
    sighting_lng = sightingInfo.at[a,'lng']

    for i, rows in stationInfo.iterrows():
        station_lat = stationInfo.at[i,'LAT']
        station_lng = stationInfo.at[i,'LNG']

        #print(sighting_lat, sighting_lng, station_lat, station_lng, stationInfo.at[i,"STATION_NAME"])
        if geopy.distance.distance((sighting_lat,sighting_lng),(station_lat,station_lng)) <= 20:
            range.write(sightingInfo.at[a,'city'] +' '+str(sightingInfo.at[a,'state']) + ' station_coord: ' + str(station_lat) + ' ' + str(station_lng) +' sighting_coord: ' + str(sighting_lat) + ' ' + str(sighting_lng)+'\n')
            count+=1
            print('Sighting ' + sightingInfo.at[a,'city'] + str(sightingInfo.at[a,'state']) + ' is in range of ' + stationInfo.at[i,'STATION_NAME'])

print('Anzahl: '+str(count))