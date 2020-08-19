import redis
import random
import string
import time
from cuncurrent.futures import ThreadPoolExecutor



def random_key(length):
    allowed_chars = string.ascii_letters + string.punctuation
    return ''.join(random.choice(allowed_chars) for x in range(length))

def reader_worker():
    while True:
        r = redis.Redis(host='localhost', port=6379, db=0, password='password')
        r.get()

def main():
    executor = ThreadPoolExecutor(max_worker=100)
    while True:
        executor.submit(writer_worker)

