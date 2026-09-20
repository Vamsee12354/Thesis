import unittest
import time
from implementation_manual import Product_cache_get

class TestProductCacheGet(unittest.TestCase):

    def setUp(self):
        self.default_expiry = 60000  # 60 seconds in milliseconds
        self.cache = Product_cache_get(expiry_time=self.default_expiry)

    def test_initialization(self):
        # Action & Verify
        self.assertIsInstance(self.cache, Product_cache_get)

    def test_set_and_get_value(self):
        # Setup
        key = 'a'
        value = 'apple'
        # Action
        self.cache.set(key, value)
        # Verify
        self.assertEqual(self.cache.get(key), value)

    def test_get_non_existent_key_returns_none(self):
        # Action & Verify
        self.assertIsNone(self.cache.get("non-existent"))

    def test_set_with_custom_ttl_and_get(self):
        # Setup
        key = "fruit"
        value = {"id": "fruit", "name": "apple"}
        ttl = 60000  # 1 minute in milliseconds
        # Action
        self.cache.set(key, value, ttl=ttl)
        # Verify
        self.assertEqual(self.cache.get(key), value)

    def test_set_with_negative_ttl_invalidates_immediately(self):
        # Setup
        key = "invalid"
        value = "should not store"
        ttl = -1000
        # Action
        self.cache.set(key, value, ttl=ttl)
        # Verify
        self.assertIsNone(self.cache.get(key))

    def test_delete_existing_key(self):
        # Setup
        key = 'a'
        value = 'apple'
        self.cache.set(key, value)
        # Action
        result = self.cache.delete(key)
        # Verify
        self.assertEqual(result, "deleted successfully")
        self.assertIsNone(self.cache.get(key))

    def test_delete_non_existent_key(self):
        # Action
        result = self.cache.delete("non-existent")
        # Verify
        self.assertEqual(result, "deleted successfully")

    def test_cleanup_clears_all_cache(self):
        # Setup
        self.cache.set('a', 'apple')
        self.cache.set('b', 'banana')
        # Action
        result = self.cache.cleanup()
        # Verify
        self.assertEqual(result, "Cleaned successfully")
        self.assertIsNone(self.cache.get('a'))
        self.assertIsNone(self.cache.get('b'))

    def test_expiry_of_cache_item(self):
        # Setup
        key = 'temp'
        value = 'data'
        short_ttl = 100  # 100 milliseconds
        self.cache.set(key, value, ttl=short_ttl)
        # Action & Verify before expiry
        self.assertEqual(self.cache.get(key), value)
        # Wait for expiry
        time.sleep(0.15)
        # Verify after expiry
        self.assertIsNone(self.cache.get(key))

    def test_set_without_ttl_uses_default_expiry(self):
        # Setup
        key = 'default_ttl'
        value = 'value'
        self.cache.set(key, value)
        # Action & Verify before expiry
        self.assertEqual(self.cache.get(key), value)
        # Wait less than expiry time
        time.sleep(0.05)
        self.assertEqual(self.cache.get(key), value)
        # Wait for expiry
        time.sleep(self.default_expiry / 1000)
        self.assertIsNone(self.cache.get(key))

if __name__ == '__main__':
    unittest.main()