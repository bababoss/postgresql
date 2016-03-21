# this python file use for insert sensor data in database

#import MyDB connection module
import MyDB
db = MyDB.DB()
import time

#query1 = "SELECT * FROM zones;"  # # SELECT query from zones table
query1 = "SELECT user_id FROM zones WHERE zone1 >= timestamp ;" #query for user accorting to date
users_date_wise=db.execute(query1)