#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# file paths
weather_path = 'sunshine_total_backup.csv'
df = pd.read_csv(weather_path, parse_dates=["time_date"])
#df.time_date = pd.to_datetime(df.time_date)
df.sort_values(by='time_date', ascending=False, inplace=True)

#%%
# hourly_suntime
plt.figure(figsize=(10,5))
plt.plot(df.time_date, df.sun_hourly, 'r.-')
plt.title('Sonnenminuten pro Stunde je Sichtung')
plt.ylabel('Sonnenminuten/Stunde')
plt.xlabel('Datum')
plt.show()

#%%
# daily_suntime
plt.figure(figsize=(10,5))
plt.plot(df.time_date, df.sun_daily, 'b.-')
plt.title('Sonnenminuten pro Tag je Sichtung')
plt.ylabel('Sonnenminuten/Tag')
plt.xlabel('Datum')
plt.show()

#%%
# condition_codes
plt.figure(figsize=(10,5))
plt.plot(df.time_date, df.condition_code, 'g.-')
plt.title('Himmelkonditionen je Sichtung')
plt.ylabel('Conditioncode')
plt.xlabel('Datum')
plt.show()
#%%