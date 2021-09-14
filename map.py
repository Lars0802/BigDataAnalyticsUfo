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
plt.figure(figsize=(16,9))
plt.plot(df.time_date, df.sun_hourly, 'r.-')
plt.title('Sonnenminuten pro Stunde je Sichtung')
plt.ylabel('Sonnenminuten/Stunde')
plt.xlabel('Datum')
plt.show()
try:
    plt.savefig('img/hourly_suntime.png', dpi=(1920/16))
except Exception as e:
    print(e)

#%%
# daily_suntime
plt.figure(figsize=(16,9))
plt.plot(df.time_date, df.sun_daily, 'b.-')
plt.title('Sonnenminuten pro Tag je Sichtung')
plt.ylabel('Sonnenminuten/Tag')
plt.xlabel('Datum')
plt.show()
try:
    plt.savefig('img/daily_suntime.png', dpi=(1920/16))
except Exception as e:
    print(e)

#%%
# condition_codes
plt.figure(figsize=(16,9))
plt.plot(df.time_date, df.condition_code, 'g.-')
plt.title('Himmelkonditionen je Sichtung')
plt.ylabel('Conditioncode')
plt.xlabel('Datum')
plt.show()
try:
    plt.savefig('img/condition_codes.png', dpi=(1920/16))
except Exception as e:
    print(e)

#%%