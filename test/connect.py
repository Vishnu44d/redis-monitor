import redis
r = redis.Redis(host='localhost', port=6379, db=0, password='password')

while True:
    r.set('foo', 1)
    r.get('foo')