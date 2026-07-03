import time

class Product_cache_get:
    def __init__(self, expiry_time):
        try:
            self.default_expiry_time = expiry_time
            self.cache = {}
        except Exception:
            self.cache = {}
            self.default_expiry_time = 0

    def set(self, key, value, ttl=None):
        try:
            if ttl is not None and ttl < 0:
                return None

            expiration = time.time() * 1000
            if ttl is not None:
                expiration += ttl
            else:
                expiration += self.default_expiry_time

            self.cache[key] = {
                'value': value,
                'expiry': expiration
            }
            return True
        except Exception:
            return None

    def get(self, key):
        try:
            if key not in self.cache:
                return None

            item = self.cache[key]
            if time.time() * 1000 > item['expiry']:
                self.delete(key)
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