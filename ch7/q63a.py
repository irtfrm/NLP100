import gzip, json, redis

redis = redis.Redis(host='localhost', port=6379, db=0)

with gzip.open('artist.json.gz','r') as fp:
  for line in fp:
    data = json.loads(line.decode('utf-8'))
    if 'tags' in data:
      for dct in data['tags']:
        redis.lpush(data['name'], json.dumps(dct))
    else:
      redis.lpush(data['name'], '')