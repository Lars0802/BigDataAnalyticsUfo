import mysql.connector
import csv
import sys

#connect to database
db = mysql.connector.connect(host="85.13.154.57", user="d03664f3", passwd="BigDataUfoPW", db="d03664f3")
res_1 = db.cursor()
res_2 = db.cursor()
statement_1 = "select city, state, date__time from sighting where not (city is null or city = '' or city = '?' or date__time is null or date__time = '' or date__time = '?')"
statement_2 = "select distinct city, state from sighting where not (city is null or city = '' or city = '?')"
file_path = 'data/sightings.csv'
file_cit = 'data/cit.csv'

#abfrage
try:
    res_1.execute(statement_1)
    rows_1 = res_1.fetchall()
    res_1.close()

    res_2.execute(statement_2)
    rows_2 = res_2.fetchall()
    res_2.close()
finally:
    db.close()

#in csv speichern
if rows_1:
    fs = open(file_path, 'w', newline = '')
    ergebnisse = csv.writer(fs)
    ergebnisse.writerows(rows_1)
    fs.close()
else:
    sys.exit("Keine Ergebnisse")

#in txt speichern
if rows_2:
    fs = open(file_cit, 'w', newline = '')
    ergebnisse = csv.writer(fs)
    ergebnisse.writerows(rows_2)
    fs.close()
else:
    sys.exit("Keine Ergebnisse")