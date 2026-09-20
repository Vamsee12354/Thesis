import time

class Product_cache_get:
    def __init__(self, expiry_time):
        self.expiry_time = expiry_time
        self.cache = {}
        self.cleanup_time = time.time() + self.expiry_time

    def set(self, key, value, ttl=None):
        if ttl is None:
            ttl = self.expiry_time
        if ttl < 0:
            return
        self.cache[key] = {
            'value': value,
            'expiry': time.time() + ttl
        }

    def get(self, key):
        if key in self.cache:
            if time.time() < self.cache[key]['expiry']:
                return self.cache[key]['value']
            else:
                del self.cache[key]
        return None

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            return "deleted successfully"
        return None

    def cleanup(self):
        self.cache.clear()
        return "Cleaned successfully"
