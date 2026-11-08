import time

class Product_cache_get:
    def __init__(self, expiry_time):
        self.cache = {}
        self.expiry_time = expiry_time

    def set(self, key, value, ttl=None):
        current_time = time.time() * 1000
        if ttl is not None and ttl <= 0:
            return
        expiry = current_time + (ttl if ttl is not None else self.expiry_time)
        self.cache[key] = {'value': value, 'expiry': expiry}

    def get(self, key):
        current_time = time.time() * 1000
        item = self.cache.get(key)
        if item is None:
            return None
        if current_time > item['expiry']:
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
