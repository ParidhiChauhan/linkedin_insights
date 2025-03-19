import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_cached_page(page_id):
    data = redis_client.get(page_id)
    return json.loads(data) if data else None

def cache_page(page_id, data, ttl=300):
    redis_client.setex(page_id, ttl, json.dumps(data))
