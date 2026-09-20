import time


class Product_cache_get:
    def __init__(self, expiry_time):
        self.expiry_time = expiry_time
        self.cache = {}

    def set(self, key, value, ttl=None):
        try:
            ttl = self.expiry_time if ttl is None else ttl
            if ttl < 0:
                if key in self.cache:
                    del self.cache[key]
                return None
            expiry = int(time.time() * 1000) + ttl
            self.cache[key] = (value, expiry)
            return value
        except Exception:
            return None

    def get(self, key):
        try:
            if key not in self.cache:
                return None
            value, expiry = self.cache[key]
            if int(time.time() * 1000) > expiry:
                del self.cache[key]
                return None
            return value
        except Exception:
            return None

    def delete(self, key):
        try:
            if key in self.cache:
                del self.cache[key]
            return "deleted successfully"
        except Exception:
            return None

    def cleanup(self):
        try:
            self.cache.clear()
            return "Cleaned successfully"
        except Exception:
            return None