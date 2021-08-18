from datetime import datetime
import pandas as pd

sighting = pd.read_csv("cit_date.csv")
station = pd.read_csv("exp_newyorkcity.csv")
result = open("result.txt", "a")

for i, rows in sighting.iterrows():
    date = datetime.strptime(station.at[i,'DATE'],'%Y-%m-%dT%H:%M:%S')