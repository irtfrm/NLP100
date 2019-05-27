import json, gzip, pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.artist
col = db.artist

for i, doc in enumerate(col.find({'tags.value': 'dance'}).sort('rating.value', pymongo.DESCENDING).limit(10)):
  print('%d位: %s' % (i+1, doc['name']))