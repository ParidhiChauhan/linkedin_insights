import redis
import json

cache = redis.StrictRedis(host='localhost', port=6379, db=0)

def cache_data(key, data, ttl=300):
    cache.setex(key, ttl, json.dumps(data))

def get_cached_data(key):
    data = cache.get(key)
    if data:
        return json.loads(data)
    return None
