# Ufo-Python
## Requirements
[Python3](https://www.python.org/downloads/)
[MySQL](https://dev.mysql.com/downloads/installer/)

```bash
pip install pandas
pip install requests
pip install geopy

db = mysql.connector.connect(host="85.13.154.57", user="d03664f3", passwd="BigDataUfoPW", db="d03664f3")

Quelle Stationen alt: https://www1.ncdc.noaa.gov/pub/data/noaa/isd-history.txt



BUGS:
header in sightings.csv hinzufügen (city,state,date__time)