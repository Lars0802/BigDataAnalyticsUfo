import requests
import json


# token: JruLOdYbPxhJVwtFUbzmXFHxzjMDKobZ

# HourlyVisibility, HourlySkyConditions local-climatological-data
# Daily Summary: GHCND
#NY WBAN:94728

try:
    req = "https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=WBAN:94728&startDate=2021-01-01&endDate=2021-01-30&boundingBox=90,-180,-90,180"
    # Stations: req_2 = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?datatypeid=ACMH&limit=1000"

    response = requests.get(req, headers={'Token': 'JruLOdYbPxhJVwtFUbzmXFHxzjMDKobZ'},allow_redirects=True)
    open("data_request.csv", "wb").write(response.content)
    print("+")

    data = response.json()
    with open("req_test.json", "w") as d:
        json.dump(data, d, indent=4)
    
except requests.exceptions.HTTPError as e:
    print("error!")
    print (e)
