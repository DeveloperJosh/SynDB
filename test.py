import SynDB

db = SynDB.load("test.db")

db.set("key1", "value1")
db.get("key1")
db.delete("key1")
db.resetdb()
db.dump() 
db.loadall() # This will load all the data from the file