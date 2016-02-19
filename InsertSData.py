# this python file use for insert sensor data in database

#import MyDB connection module
import MyDB
db = MyDB.DB()
import time
user_id=1027
zone_id = ['zone1','zone2','zone3','zone4']
list = ['1021','2022','2023','2024']
#db.execute("INSERT INTO login_out (user_id,zone1) \
#      VALUES ( %s, NOW() )", [list[0]]);

i=0
while (i<len(list)):
    if zone_id[i]=='zone1':
        db.execute("INSERT INTO login_out (user_id,zone1) \
              VALUES ( %s, NOW() )", [list[i]]);
        db.commit()
        print "zone is", i
        i=i+1
        time.sleep(1)
        print 'i is',i

    elif zone_id[i]=='zone2':
        db.execute("INSERT INTO login_out (user_id,zone2) \
              VALUES ( %s, NOW() )", [list[i]]);
        db.commit()
        print "zone is", i
        i=i+1
        time.sleep(1)
        print 'i is',i

    elif zone_id[i]=='zone3':
        db.execute("INSERT INTO login_out (user_id,zone3) \
              VALUES ( %s, NOW() )", [list[i]]);
        db.commit()
        print "zone is", i
        i=i+1
        time.sleep(1)
        print 'i is',i

    elif zone_id[i]=='zone4':
        db.execute("INSERT INTO login_out (user_id,zone4) \
              VALUES ( %s, NOW() )", [list[i]]);
        db.commit()
        print "zone is", i
        i=i+1
        time.sleep(1)
        print 'i is',i

db.execute("INSERT INTO login_out (user_id,zone4) \
                    VALUES ( %s, NOW() )", [list[0]]);
db.commit()
print "Records created successfully";
print zone_id
db.close()