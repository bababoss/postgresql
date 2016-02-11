

import psycopg2
import sys

try:
    conn = psycopg2.connect("host='localhost' dbname='myproject' user='myprojectuser' password='password'")
    print "Database is connected"
except:
    print "I am unable to connect to the database"

cursor = conn.cursor()
query = "INSERT INTO test (num, data) VALUES (%s, %s, %s)",('ghh','kdjij','kddsglk');
results = cursor.execute(query)
print cursor.fetchall()


