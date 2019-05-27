import json, gzip, pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.artist
col = db.artist

for doc in col.find({'aliases.name': '女王'}):
  print(doc)