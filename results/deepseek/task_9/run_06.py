import time

class Product_cache_get:
    def __init__(self, expiry_time):
        self.cache = {}
        self.expiry_time = expiry_time

    def set(self, key, value, ttl=None):
        if ttl is None:
            ttl = self.expiry_time
        if ttl < 0:
            return
        self.cache[key] = {'value': value, 'expiry': time.time() + ttl / 1000}

    def get(self, key):
        if key not in self.cache:
            return None
        item = self.cache[key]
        if time.time() > item['expiry']:
            del self.cache[key]
            return None
        return item['value']

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
        return "deleted successfully"

    def cleanup(self):
        self.cache.clear()
        return "Cleaned successfully"