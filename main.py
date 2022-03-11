import pymongo
from pymongo import MongoClient
import datetime as dt

client = MongoClient()

db = client.pydb  # will create db if doesn't exist
users = db.users  # will create collection(table) if doesn't exist
user = {'name':'nadah', 'uniID':20180309, 'gender':'fem', 'skills':['python', 'java', 'c++']}
#user_id = users.insert_one(user).inserted_id  # add just one document (element) at a time
#print(user_id)

now = dt.datetime.now()
users_list = [{'name':'n1', 'uniID': 1234, 'gender': 'fem', 'skills':['c++', 'c', 'sql'], 'date': now},
              {'name':'usernew', 'uniID': 45678, 'gender': 'fem', 'skills':['html', 'css', 'php'], 'date': now}]

#users.insert_many(users_list)

# note for conditions to find ->  {'something' : {'$e(equals), $ne(not equals), $lte(less than or equal), $exists'}
count = users.count_documents({'name':'nadah'})
#print(count)
find = users.find({})
#print(find[0]['skills'])

print(users.count_documents({'date':{'$exists':False}}))

db.users.create_index([('uniID', pymongo.ASCENDING)])
print(db.users.index_information())

