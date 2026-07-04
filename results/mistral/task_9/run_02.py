
from time import time

class ProductCacheGet:
    def __init__(self, expiry_time):
        self.expiry_time = expiry_time
        self.cache = {}

    def set(self, key, value, ttl=None):
        if ttl is None:
            ttl = self.expiry_time
        if ttl <= 0:
            return
        expiry = time() * 1000 + ttl
        self.cache[key] = (value, expiry)

    def get(self, key):
        if key not in self.cache:
            return None
        value, expiry = self.cache[key]
        if time() * 1000 > expiry:
            del self.cache[key]
            return None
        return value

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            return "deleted successfully"
        return None

    def cleanup(self):
        self.cache.clear()
        return "Cleaned successfully"
from time import time

 