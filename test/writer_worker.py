import redis
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor



def random_key(length):
    allowed_chars = string.ascii_letters + string.punctuation
    return ''.join(random.choice(allowed_chars) for x in range(length))

def writer_worker():
    while True:
        r = redis.Redis(host='localhost', port=6379, db=0, password='password')
        key = random_key(random.randint(10, 20))
        value = random.randint(1, 9999)
        exp = random.randint(1, 3)
        r.set(key, value, exp)

def main():
    executor = ThreadPoolExecutor(max_workers=100)
    while True:
        executor.submit(writer_worker)

if __name__ == "__main__":
    main()