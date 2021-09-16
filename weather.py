# Lars Thomsen, anhqn
# 02.09.2021

from datetime import datetime, timedelta
from meteostat import Point, Hourly, Daily
import pandas as pd
from csv import reader
import os

# file paths
file_path_final = 'data/sunshine_total.csv'
file_path_lnglat = 'data/cities_coords.csv'
file_path_sight = 'data/sightings.csv'

# del if exists
try:
    os.remove(file_path_final)
except:
    pass

# functions
def get_city(): # returns city name
    return row[0]

def get_state(): # returns state name
    return row[1]

def get_datetime(): # returns date and time
    date_time_str = row[2]
    for formats in ('%m/%d/%y %H:%M', '%m/%d/%y'):
        try:
            return datetime.strptime(date_time_str, formats)
        except:
            pass

def get_lat(city, state): # returns latitude of given city-state tuple
    with open(file_path_lnglat, 'r',) as lnglat_reader:
        coords = reader(lnglat_reader)
        for row in coords:
            if row[0].lower() == city:
                if row[1].lower() == state:
                    return row[2]

def get_lng(city, state): # returns longitude of given city-state tuple
    with open(file_path_lnglat, 'r') as lnglat_reader:
        coords = reader(lnglat_reader)
        for row in coords:
            if row[0].lower() == city:
                if row[1].lower() == state:
                    return row[3]

def write_suntime(city, state, time, sunshine_hourly, sunshine_daily, condition_code): # writes returned suntime in file
    file_sun = open(file_path_final, 'a')
    file_sun.write(str(city)+', '+str(state)+', '+str(time)+', H: '+str(sunshine_hourly)+', D: '+str(sunshine_daily)+', COCO: '+str(condition_code)+'\n')
    file_sun.close()


with open(file_path_sight, 'r') as sighting_reader:
    sightings = reader(sighting_reader)
    counter = 1
    for row in sightings:      
        try:
            # get city, state, timedate, lng and lat
            city = get_city().replace(' ', '').lower()
            state = get_state().replace(' ', '').lower()
            time_start = get_datetime()
            time_end = time_start + timedelta(seconds=1)
            lat = get_lat(city, state)
            lng = get_lng(city, state)

            # def location
            location = Point(float(lat), float(lng))

            # get results as df
            result_hourly = Hourly(location, time_start, time_end)
            result_daily = Daily(location, time_start, time_end)

            # get hourly data
            data_hourly = result_hourly.fetch()
            if data_hourly.empty:
                sunshine_hourly = 'NaN'
                condition_code = 'NaN'
            else:
                sunshine_hourly = data_hourly.to_string(columns=['tsun'], index_names=None, header=False, index=False)
                condition_code = data_hourly.to_string(columns=['coco'], index_names=None, header=False, index=False)

            # get daily data
            data_daily = result_daily.fetch()
            if data_daily.empty:
                sunshine_daily = 'NaN'
            else:
                sunshine_daily = data_daily.to_string(columns=['tsun'], index_names=None, header=False, index=False)

            # check for numbers and write to csv

            x1 = float(sunshine_hourly)
            x2 = float(sunshine_daily)
            x3 = float(condition_code)
            #print(x3)
            #print(pd.isna(x3))

            if not pd.isna(x1) or not pd.isna(x2) or not pd.isna(x3): # true if value is number
                df = pd.DataFrame({'city' : [city],
                                    'state' : [state],
                                    'time_date' : [time_start],
                                    'sun_hourly' : [sunshine_hourly],
                                    'sun_daily' : [sunshine_daily],
                                    'condition_code' : [condition_code]})
                
                df.to_csv(file_path_final, mode='a', index=False, header=not os.path.exists(file_path_final))      
                #write_suntime(city, state, time_start, sunshine_hourly, sunshine_daily, condition_code)

            # clear df and cache
            data_hourly = pd.DataFrame()
            data_daily = pd.DataFrame()
            df = pd.DataFrame()
            if counter % 100 == 0:
                Daily.clear_cache(60)
                Hourly.clear_cache(60)

            print(counter)
            counter+=1
            #if counter == 5:
                #break
        except Exception as e:
            print(e)
            counter+=1
            continue