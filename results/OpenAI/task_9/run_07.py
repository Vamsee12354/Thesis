import time


class ProductCacheGet:
    def __init__(self, expiry_time):
        self.expiry_time = expiry_time
        self.cache = {}

    def set(self, key, value, ttl=None):
        try:
            ttl = ttl if ttl is not None else self.expiry_time
            if ttl < 0:
                if key in self.cache:
                    del self.cache[key]
                return None
            expiry_timestamp = int(time.time() * 1000) + ttl
            self.cache[key] = (value, expiry_timestamp)
            return value
        except Exception:
            return None

    def get(self, key):
        try:
            if key not in self.cache:
                return None
            value, expiry_timestamp = self.cache[key]
            if int(time.time() * 1000) > expiry_timestamp:
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
            return None
        except Exception:
            return None

    def cleanup(self):
        try:
            self.cache.clear()
            return "Cleaned successfully"
        except Exception:
            return None