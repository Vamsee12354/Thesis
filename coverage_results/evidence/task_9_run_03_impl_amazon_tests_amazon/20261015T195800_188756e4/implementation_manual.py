import time

class Product_cache_get:
    def __init__(self, expiry_time):
        self.expiry_time = expiry_time
        self.cache = {}
        self.cache_expiry = {}
        self.last_cleanup = time.time()

    def set(self, key, value, ttl=None):
        if ttl is None:
            ttl = self.expiry_time
        if ttl < 0:
            return None
        self.cache[key] = value
        self.cache_expiry[key] = time.time() + ttl / 1000
        return value

    def get(self, key):
        if key not in self.cache:
            return None
        if time.time() > self.cache_expiry.get(key, 0):
            self.delete(key)
            return None
        return self.cache[key]

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            del self.cache_expiry[key]
            return "deleted successfully"
        return None

    def cleanup(self):
        current_time = time.time()
        keys_to_delete = [
            key for key, expiry in self.cache_expiry.items() if current_time > expiry
        ]
        for key in keys_to_delete:
            self.delete(key)
        self.last_cleanup = current_time
        return "Cleaned successfully"
