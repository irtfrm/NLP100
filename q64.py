import json, gzip, pymongo
from pymongo import MongoClient

def load_gzip(file_name, collection):
  with gzip.open(file_name,'r') as fp:
    for line in fp:
      data = json.loads(line.decode('utf-8'))
      collection.insert_one(data)

client = MongoClient('localhost', 27017)
db = client.artist
collection = db.artist

load_gzip('artist.json.gz', collection)

collection.create_index([('name', pymongo.ASCENDING)])
collection.create_index([('aliases.name', pymongo.ASCENDING)])
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])