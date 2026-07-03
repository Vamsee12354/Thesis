import time

class Product_cache_get:
    def __init__(self, expiry_time):
        try:
            self.default_ttl = expiry_time
            self.cache = {}
        except Exception:
            self.default_ttl = None
            self.cache = {}

    def set(self, key, value, ttl=None):
        try:
            if ttl is not None and ttl < 0:
                return None

            current_time = time.time() * 1000
            effective_ttl = ttl if ttl is not None else self.default_ttl

            if effective_ttl is not None:
                expiration_time = current_time + effective_ttl
            else:
                expiration_time = float('inf')

            self.cache[key] = {
                'value': value,
                'expiry': expiration_time
            }
        except Exception:
            return None

    def get(self, key):
        try:
            if key not in self.cache:
                return None

            item = self.cache[key]
            current_time = time.time() * 1000

            if current_time > item['expiry']:
                del self.cache[key]
                return None

            return item['value']
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
