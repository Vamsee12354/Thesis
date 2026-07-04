import time

class Product_cache_get:
    def __init__(self, expiry_time):
        self.cache = {}
        self.default_expiry = expiry_time

    def set(self, key, value, ttl=None):
        expiry = ttl if ttl is not None else self.default_expiry
        if expiry < 0:
            return
        self.cache[key] = {
            'value': value,
            'expiry': time.time() * 1000 + expiry
        }

    def get(self, key):
        item = self.cache.get(key)
        if item is None:
            return None
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
