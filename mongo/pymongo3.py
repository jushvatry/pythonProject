from pymongo import MongoClient

conn = MongoClient('localhost',27017)

db = conn.stu

myset = db.class4

cursor = myset.find()
for i in cursor:
    myset.update({'$set':{'_id':i['_id']}},
        


        )
