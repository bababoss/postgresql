import MyDB
db = MyDB.DB()

#query = "ALTER TABLE Measurement ADD COLUMN time_stamp timestamp;"
db.execute(query)

db.commit()
db.close()