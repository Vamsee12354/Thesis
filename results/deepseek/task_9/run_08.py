import time

class Product_cache_get:
    def __init__(self, expiry_time):
        self.cache = {}
        self.default_expiry = expiry_time

    def set(self, key, value, ttl=None):
        if ttl is not None and ttl < 0:
            return
        expiry = time.time() * 1000 + (ttl if ttl is not None else self.default_expiry)
        self.cache[key] = {'value': value, 'expiry': expiry}

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