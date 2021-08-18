import mysql.connector

#connect to database
db = mysql.connector.connect(host="85.13.154.57", user="d03664f3", passwd="BigDataUfoPW", db="d03664f3")
mycursor = db.cursor()

statement = "select distinct city, state, date__time from sighting where not (city is null or city = '' or city = '?') and city like '%new york%'"

#query
mycursor.execute(statement)

#save cities in txt
cities_date = open("cit_date.txt", "a")
cities = open("cit.txt", "a")
cities2 = open("cit2.txt", "a")
count = 0

cities.write('\n')
cities2.write('\n')

for x in mycursor:
    cities_date.write(x[0]+', '+x[1]+', '+x[2]+'\n')


#for x in mycursor:
#    if count < 14000:
#        cities.write(x[0]+', '+x[1]+'\n')
#    else:
#        cities2.write(x[0]+', '+x[1]+'\n')
#    count += 1