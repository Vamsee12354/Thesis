import time

class Product_cache_get:
    def __init__(self, expiry_time):
        self.cache = {}
        self.expiry_time = expiry_time

    def set(self, key, value, ttl=None):
        current_time = int(time.time() * 1000)
        expiry = current_time + (ttl if ttl is not None else self.expiry_time)
        if expiry <= current_time:
            return
        self.cache[key] = {'value': value, 'expiry': expiry}

    def get(self, key):
        current_time = int(time.time() * 1000)
        if key not in self.cache:
            return None
        cached_item = self.cache[key]
        if cached_item['expiry'] <= current_time:
            del self.cache[key]
            return None
        return cached_item['value']

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            return "deleted successfully"
        return None

    def cleanup(self):
        self.cache.clear()
        return "Cleaned successfully"