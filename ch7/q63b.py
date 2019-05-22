import redis, json


def load_list(lst):
  ans = []
  for text in lst:
    if text == b'': continue
    ans.append(json.loads(text.decode('utf-8')))
  
  return ans

redis = redis.Redis(host='localhost', port=6379, db=0)
res = redis.lrange('Michael Jackson', 0, 100)
print(load_list(res))