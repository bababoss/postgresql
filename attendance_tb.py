import MyDB
db = MyDB.DB()

try:
    db.execute("CREATE TABLE attendance_tb (user_id INT NOT NULL, dates TIMESTAMPTZ, work_hour TIME, extra_hour TIME);")
    print "table created successfully"
except:
    db.conn.rollback()
    db.execute("DROP TABLE zones")
    print "Drop database successfully"
    db.execute("CREATE TABLE attendance_tb (user_id INT NOT NULL, dates TIMESTAMPTZ, work_hour TIME, extra_hour TIME);")
    print "Drop database and again create successfully"
db.commit()
db.close()