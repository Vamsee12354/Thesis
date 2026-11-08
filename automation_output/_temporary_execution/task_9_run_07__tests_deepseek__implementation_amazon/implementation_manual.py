from time import time
from threading import Timer

class Product_cache_get:
    def __init__(self, expiry_time):
        self.expiry_time = expiry_time
        self.cache = {}

    def set(self, key, value, ttl=None):
        if ttl is None:
            ttl = self.expiry_time
        if ttl < 0:
            return
        expiry = time() + ttl / 1000.0
        self.cache[key] = (value, expiry)
        Timer((expiry - time()), self.delete, args=[key]).start()

    def get(self, key):
        if key in self.cache:
            value, expiry = self.cache[key]
            if time() < expiry:
                return value
            else:
                self.delete(key)
        return None

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            return "deleted successfully"
        return None

    def cleanup(self):
        self.cache.clear()
        return "Cleaned successfully"
