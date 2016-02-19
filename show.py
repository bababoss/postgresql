
#import MyDB connection module
import MyDB
db = MyDB.DB()
zone_id = ['zone1','zone2','zone3','zone4','zone5']

#query to database to select device
query1 = "SELECT * FROM login_out;"
query2 = "SELECT * FROM login_out WHERE zone1 >= timestamp '2016-02-17 T00:00:00+0000';"
query_z1 = "SELECT user_id FROM login_out WHERE zone1 >= timestamp '2016-02-19';"
query_z2 = "SELECT user_id FROM login_out WHERE zone2 >= timestamp '2016-02-18';"
query_z3 = "SELECT user_id FROM login_out WHERE zone3 >= timestamp '2016-02-19';"
query_z4 = "SELECT user_id FROM login_out WHERE zone4 >= timestamp '2016-02-19';"
#execute the query

#zone1 user of date 2016-02-19
i=0
while i<len(zone_id):
    if zone_id[i]=='zone1':
        print '%s user of date 2016-02-19',zone_id[i]
        db.execute(query_z1)
        print db.cursor.fetchall()

    elif zone_id[i]=='zone2':
        print '%s user of date 2016-02-19',zone_id[i]
        db.execute(query_z2)
        print db.cursor.fetchall()

    elif zone_id[i]=='zone3':
        print '%s user of date 2016-02-19',zone_id[i]
        db.execute(query_z3)
        print db.cursor.fetchall()

    elif zone_id[i]=='zone4':
        print '%s user of date 2016-02-19',zone_id[i]
        db.execute(query_z4)
        print db.cursor.fetchall()
    i=i+1




db.execute(query_z1)
# print data
print "print zone1 user_id"
print db.cursor.fetchall()
# commit database
db.commit()
db.close()
