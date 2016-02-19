import MyDB
db = MyDB.DB()

try:
    db.execute("CREATE TABLE zones (user_id INT NOT NULL, zone1 TIMESTAMPTZ, zone2 TIMESTAMPTZ, zone3 TIMESTAMPTZ, zone4 TIMESTAMPTZ);")
    print "table created successfully"
except:
    db.conn.rollback()
    db.execute("DROP TABLE zones")
    print "Drop database successfully"
    db.execute("CREATE TABLE login_out (user_id INT NOT NULL, zone1 TIMESTAMPTZ, zone2 TIMESTAMPTZ, zone3 TIMESTAMPTZ, zone4 TIMESTAMPTZ);")
    print "Drop database and again create successfully"
db.commit()
db.close()