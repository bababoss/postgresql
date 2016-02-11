import MyDB
db = MyDB.DB()

db.conn.rollback()
db.execute("DROP TABLE Measurement")
print "drop Measurement database successfully"

db.commit()
db.close()