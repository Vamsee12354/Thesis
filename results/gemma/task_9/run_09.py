import time

class Product_cache_get:
    def __init__(self, expiry_time):
        self.default_expiry = expiry_time
        self.cache = {}

    def set(self, key, value, ttl=None):
        try:
            now = time.time() * 1000
            if ttl is not None and ttl < 0:
                return

            actual_ttl = ttl if ttl is not None else self.default_expiry
            expiration_time = now + actual_ttl
            self.cache[key] = {
                'value': value,
                'expires_at': expiration_time
            }
        except Exception:
            return None

    def get(self, key):
        try:
            if key not in self.cache:
                return None

            item = self.cache[key]
            now = time.time() * 1000

            if now > item['expires_at']:
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