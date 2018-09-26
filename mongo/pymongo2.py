from pymongo import MongoClient

conn = MongoClient('localhost',27017)

db = conn.stu

myset = db.class1

# index = myset.ensure_index([('name',1)])
# print(index)

# myset.drop_index('name_1')

# myset.ensure_index('name',1,name='myIndex',unique=True)
# for i in myset.list_indexes():
#     print(i)

myset1 = db.class4

p = [{'$group':{'_id':'king','count':{'$sum':1}}},
    {'$match':{'count':{'$gt':1}}
    }
    

]

cursor = myset.aggregate(p)
print(cursor)
for i in cursor:
    print(i)
