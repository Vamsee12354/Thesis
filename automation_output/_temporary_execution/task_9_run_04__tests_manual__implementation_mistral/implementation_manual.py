
class ProductCacheGet:
    def __init__(self, expiry_time):
        self.expiry_time = expiry_time
        self.cache = {}

    def set(self, key, value, ttl=None):
        if ttl is None:
            ttl = self.expiry_time
        if ttl <= 0:
            return
        self.cache[key] = {
            'value': value,
            'expiry': ttl
        }

    def get(self, key):
        if key not in self.cache:
            return None
        item = self.cache[key]
        return item['value']

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            return "deleted successfully"
        return None

    def cleanup(self):
        self.cache.clear()
        return "Cleaned successfully"
class Product_cache_get(ProductCacheGet):
    pass
Product_cache_get = Product_cache_get
del ProductCacheGet