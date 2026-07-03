import time

class Product_cache_get:
    def __init__(self, expiry_time):
        try:
            self.default_expiry = expiry_time
            self.cache = {}
        except Exception:
            self.cache = {}

    def set(self, key, value, ttl=None):
        try:
            if ttl is not None and ttl < 0:
                return

            current_time = time.time() * 1000
            if ttl is None:
                expiration = current_time + self.default_expiry
            else:
                expiration = current_time + ttl

            self.cache[key] = {
                'value': value,
                'expires_at': expiration
            }
        except Exception:
            pass

    def get(self, key):
        try:
            if key not in self.cache:
                return None

            item = self.cache[key]
            current_time = time.time() * 1000

            if current_time > item['expires_at']:
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