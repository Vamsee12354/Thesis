from implementation_manual import Product_cache_get
import unittest
import time

class TestProductCacheGet(unittest.TestCase):

    def test_initialization_with_positive_expiry_time(self):
        cache = Product_cache_get(expiry_time=60000)
        self.assertIsInstance(cache, Product_cache_get)

    def test_initialization_with_zero_expiry_time(self):
        cache = Product_cache_get(expiry_time=0)
        self.assertIsInstance(cache, Product_cache_get)

    def test_initialization_with_negative_expiry_time(self):
        cache = Product_cache_get(expiry_time=-1000)
        self.assertIsInstance(cache, Product_cache_get)

    def test_set_and_get_basic_value(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('a', 'apple')
        self.assertEqual(cache.get('a'), 'apple')

    def test_get_nonexistent_key(self):
        cache = Product_cache_get(expiry_time=60000)
        self.assertIsNone(cache.get('nonexistent'))

    def test_set_with_custom_ttl(self):
        cache = Product_cache_get(expiry_time=60000)
        custom_value = {"id": "fruit", "name": "apple"}
        cache.set("fruit", custom_value, ttl=60000)
        self.assertEqual(cache.get("fruit"), custom_value)

    def test_set_with_negative_custom_ttl(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('a', 'apple', ttl=-1000)
        self.assertIsNone(cache.get('a'))

    def test_set_with_zero_custom_ttl(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('a', 'apple', ttl=0)
        self.assertIsNone(cache.get('a'))

    def test_delete_existing_key(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('a', 'apple')
        result = cache.delete('a')
        self.assertEqual(result, "deleted successfully")
        self.assertIsNone(cache.get('a'))

    def test_delete_nonexistent_key(self):
        cache = Product_cache_get(expiry_time=60000)
        result = cache.delete('nonexistent')
        self.assertEqual(result, "deleted successfully")

    def test_cleanup_entire_cache(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('a', 'apple')
        cache.set('b', 'banana')
        result = cache.cleanup()
        self.assertEqual(result, "Cleaned successfully")
        self.assertIsNone(cache.get('a'))
        self.assertIsNone(cache.get('b'))

    def test_cleanup_on_empty_cache(self):
        cache = Product_cache_get(expiry_time=60000)
        result = cache.cleanup()
        self.assertEqual(result, "Cleaned successfully")

    def test_expiry_time_enforcement(self):
        cache = Product_cache_get(expiry_time=100)
        cache.set('temp', 'value')
        time.sleep(0.2)
        self.assertIsNone(cache.get('temp'))

    def test_custom_ttl_expiry(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('temp', 'value', ttl=100)
        time.sleep(0.2)
        self.assertIsNone(cache.get('temp'))

    def test_overwrite_existing_key(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('a', 'apple')
        cache.set('a', 'apricot')
        self.assertEqual(cache.get('a'), 'apricot')

    def test_multiple_keys_in_cache(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('a', 'apple')
        cache.set('b', 'banana')
        cache.set('c', 'cherry')
        self.assertEqual(cache.get('a'), 'apple')
        self.assertEqual(cache.get('b'), 'banana')
        self.assertEqual(cache.get('c'), 'cherry')