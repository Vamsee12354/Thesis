
class Product_cache_get:
    def __init__(self, expiry_time):
        self.expiry_time = expiry_time
        self.cache = {}

    def set(self, key, value, ttl=None):
        if ttl is None:
            ttl = self.expiry_time
        if ttl <= 0:
            return None
        self.cache[key] = {
            'value': value,
            'expiry': (time.time() * 1000) + ttl
        }

    def get(self, key):
        if key not in self.cache:
            return None
        item = self.cache[key]
        if time.time() * 1000 > item['expiry']:
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

import time
time_module = time
time = time_module