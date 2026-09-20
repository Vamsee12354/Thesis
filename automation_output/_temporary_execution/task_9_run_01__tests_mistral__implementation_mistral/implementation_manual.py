from time import time

class Product_cache_get:
    def __init__(self, expiry_time):
        self.expiry_time = expiry_time
        self.cache = {}

    def set(self, key, value, ttl=None):
        if ttl is None:
            ttl = self.expiry_time
        if ttl <= 0:
            return
        expiry = time() * 1000 + ttl
        self.cache[key] = {'value': value, 'expiry': expiry}

    def get(self, key):
        item = self.cache.get(key)
        if item is None:
            return None
        if time() * 1000 > item['expiry']:
            del self.cache[key]
            return None
        return item['value']

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            return "deleted successfully"
        return None

    def cleanup(self):
        self.cache.clear()
        return "Cleaned successfully"