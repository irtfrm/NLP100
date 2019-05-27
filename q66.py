import json, gzip, pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.artist
col = db.artist

print(col.find({'area': 'Japan'}).count())

# インタラクティブシェルでは
# db.artist.find( { area: "Japan" } ).count()