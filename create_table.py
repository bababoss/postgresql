import MyDB
db = MyDB.DB()

try:
    db.execute("CREATE TABLE Measurement (time_stamp TIMESTAMP NOT NULL, MotionMeasure INT, TempMeasure INT, LightSensitivity INT,  ZoneID VARCHAR);")
    print "table created successfully"
except:
    db.conn.rollback()
    db.execute("DROP TABLE Measurement")
    print "Drop database successfully"
    db.execute("CREATE TABLE Measurement (time_stamp TIMESTAMP NOT NULL, MotionMeasure INT, TempMeasure INT, LightSensitivity INT);")
    print "Drop database and again create successfully"
db.commit()
db.close()