import unittest
import time
from implementation_manual import Product_cache_get

class TestProductCacheGet(unittest.TestCase):

    def setUp(self):
        self.expiry_time = 1000  # 1 second expiry for tests
        self.cache = Product_cache_get(self.expiry_time)

    def test_initialization(self):
        # Action & Verification
        self.assertIsInstance(self.cache, Product_cache_get)

    def test_set_and_get_value(self):
        # Setup
        key = 'a'
        value = 'apple'
        # Action
        self.cache.set(key, value)
        result = self.cache.get(key)
        # Verification
        self.assertEqual(result, value)

    def test_get_non_existent_key_returns_none(self):
        # Action
        result = self.cache.get('non-existent')
        # Verification
        self.assertIsNone(result)

    def test_set_with_custom_ttl_and_get(self):
        # Setup
        key = 'fruit'
        value = {"id": "fruit", "name": "apple"}
        ttl = 60000  # 1 minute in ms
        # Action
        self.cache.set(key, value, ttl=ttl)
        result = self.cache.get(key)
        # Verification
        self.assertEqual(result, value)

    def test_set_with_negative_ttl_invalidates_immediately(self):
        # Setup
        key = 'neg'
        value = 'invalid'
        ttl = -1000
        # Action
        self.cache.set(key, value, ttl=ttl)
        result = self.cache.get(key)
        # Verification
        self.assertIsNone(result)

    def test_delete_existing_key(self):
        # Setup
        key = 'a'
        value = 'apple'
        self.cache.set(key, value)
        # Action
        result = self.cache.delete(key)
        get_result = self.cache.get(key)
        # Verification
        self.assertEqual(result, "deleted successfully")
        self.assertIsNone(get_result)

    def test_delete_non_existent_key(self):
        # Action
        result = self.cache.delete('non-existent')
        # Verification
        self.assertEqual(result, "deleted successfully")

    def test_cleanup_clears_all_cache(self):
        # Setup
        self.cache.set('a', 'apple')
        self.cache.set('b', 'banana')
        # Action
        result = self.cache.cleanup()
        get_a = self.cache.get('a')
        get_b = self.cache.get('b')
        # Verification
        self.assertEqual(result, "Cleaned successfully")
        self.assertIsNone(get_a)
        self.assertIsNone(get_b)

    def test_expiry_of_cache_item(self):
        # Setup
        key = 'temp'
        value = 'data'
        ttl = 500  # 0.5 seconds
        self.cache.set(key, value, ttl=ttl)
        # Action & Verification before expiry
        self.assertEqual(self.cache.get(key), value)
        # Wait for expiry
        time.sleep(0.6)
        # Verification after expiry
        self.assertIsNone(self.cache.get(key))

    def test_set_without_ttl_uses_default_expiry(self):
        # Setup
        key = 'default_ttl'
        value = 'default'
        self.cache.set(key, value)
        # Action & Verification before expiry
        self.assertEqual(self.cache.get(key), value)
        # Wait for expiry_time + small buffer
        time.sleep(self.expiry_time / 1000 + 0.1)
        # Verification after expiry
        self.assertIsNone(self.cache.get(key))

if __name__ == '__main__':
    unittest.main()