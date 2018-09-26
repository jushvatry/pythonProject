from pymongo import MongoClient

conn = MongoClient('localhost',27017)

db = conn.stu

myset = db.class4
# myset.insert({'name':'张铁林',"age":55,'sex':'m'})

# myset.insert([{"name":'张国立','king':'康熙'},{"name":'陈道明','king':'康熙'}])
# myset.insert_many([{"name":'唐国强','king':'雍正'},{"name":'陈建斌','king':'雍正'}])
# myset.save({'_id':1,"name":'聂远','king':'乾隆'})
# myset.save({'_id':1,"name":'吴奇隆','king':'四爷'})
# myset.save({'_id':1,"name":'赵四','king':'四爷'})
# print(dir(myset))
# cursor = myset.find({},{'_id':0})
# print(cursor)
# for i in cursor:
#     print(i['name'],'---------',i['king'])

conn.close()