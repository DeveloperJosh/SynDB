import syndb

db = syndb.load("test.db", False) ## If not set to True, the database will not be dumped automatically.

db.set("test", "test")
db.set("test2" , "test2")
db.set("test3" , "test3")
db.dump()
db.loadall()