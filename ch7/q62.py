import redis

redis = redis.Redis(host='localhost', port=6379, db=0)

for key in redis.scan_iter():
  area = redis.get(key)
  if area == b'Japan':
    print(key.decode())