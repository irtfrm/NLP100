import json, gzip, pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.artist
col = db.artist

for doc in col.find({'name': 'Queen'}):
  print(doc)

# インタラクティブシェルでは
# db.artist.find( { name: "Queen" } )