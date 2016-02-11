# this python file use for insert sensor data in database

#import MyDB connection module
import MyDB
db = MyDB.DB()
i=12
j=22
k=33
db.execute("INSERT INTO Measurement (time_stamp,MotionMeasure,TempMeasure,LightSensitivity,ZoneID) \
      VALUES (NOW(), %s, %s, %s,'room1' )", [i,j,k]);

db.execute("INSERT INTO Measurement (time_stamp,MotionMeasure,TempMeasure,LightSensitivity,ZoneID) \
      VALUES (NOW(),14, 35, 47, 'room2' )");

db.execute("INSERT INTO Measurement (time_stamp,MotionMeasure,TempMeasure,LightSensitivity,ZoneID) \
      VALUES (NOW(), 14, 35, 47, 'room3' )");

db.execute("INSERT INTO Measurement (time_stamp,MotionMeasure,TempMeasure,LightSensitivity,ZoneID) \
      VALUES (NOW(), 16, 36, 48, 'room4' )");


db.commit()
print "Records created successfully";
db.close()