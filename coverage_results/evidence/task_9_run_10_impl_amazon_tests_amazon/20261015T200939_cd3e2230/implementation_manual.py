from time import time
from threading import Lock

class Product_cache_get:
    def __init__(self, expiry_time):
        self.expiry_time = expiry_time
        self.cache = {}
        self.lock = Lock()

    def set(self, key, value, ttl=None):
        with self.lock:
            if ttl is None:
                ttl = self.expiry_time
            if ttl <= 0:
                return
            self.cache[key] = {'value': value, 'expiry': time() + ttl / 1000}

    def get(self, key):
        with self.lock:
            if key in self.cache:
                if time() > self.cache[key]['expiry']:
                    del self.cache[key]
                    return None
                return self.cache[key]['value']
            return None

    def delete(self, key):
        with self.lock:
            if key in self.cache:
                del self.cache[key]
                return "deleted successfully"
            return None

    def cleanup(self):
        with self.lock:
            self.cache.clear()
            return "Cleaned successfully"
