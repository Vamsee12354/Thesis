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

            now = time.time() * 1000
            if ttl is None:
                expiration = now + self.default_expiry
            else:
                expiration = now + ttl

            self.cache[key] = {
                "value": value,
                "expiry": expiration
            }
        except Exception:
            pass

    def get(self, key):
        try:
            if key not in self.cache:
                return None

            item = self.cache[key]
            now = time.time() * 1000

            if now > item["expiry"]:
                del self.cache[key]
                return None

            return item["value"]
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