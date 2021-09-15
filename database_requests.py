#Lars Thomsen, anhqn
#02.09.2021

import mysql.connector
import csv
import sys

#connect to database
db = mysql.connector.connect(host="85.13.154.57", user="d03664f3", passwd="BigDataUfoPW", db="d03664f3")
res = db.cursor()
statement = "select city, state, date__time from sighting where not (city is null or city = '' or city = '?' or date__time is null or date__time = '' or date__time = '?')"
file_path = 'data/sightings.csv'

#abfrage
try:
    res.execute(statement)
    rows = res.fetchall()
finally:
    db.close()

#in csv speichern
if rows:
    fs = open(file_path, 'w', newline = '')
    ergebnisse = csv.writer(fs)
    ergebnisse.writerows(rows)
    fs.close()
else:
    sys.exit("Keine Ergebnisse")