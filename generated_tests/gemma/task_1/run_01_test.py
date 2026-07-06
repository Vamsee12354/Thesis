import unittest
import time
from implementation_manual import Product_cache_get

class TestProductCacheGet(unittest.TestCase):

    def setUp(self):
        self.default_expiry = 60000
        self.cache = Product_cache_get(expiry_time=self.default_expiry)

    def test_set_and_get_happy_path(self):
        self.cache.set('a', 'apple')
        self.assertEqual(self.cache.get('a'), 'apple')

    def test_get_non_existent_key(self):
        self.assertIsNone(self.cache.get('non-existent'))

    def test_set_with_custom_ttl(self):
        product_data = {"id": "fruit", "name": "apple"}
        self.cache.set("fruit", product_data, ttl=60000)
        self.assertEqual(self.cache.get("fruit"), product_data)

    def test_set_with_negative_ttl_invalidates_immediately(self):
        self.cache.set('expired', 'value', ttl=-1)
        self.assertIsNone(self.cache.get('expired'))

    def test_delete_key(self):
        self.cache.set('a', 'apple')
        result = self.cache.delete('a')
        self.assertEqual(result, "deleted successfully")
        self.assertIsNone(self.cache.get('a'))

    def test_cleanup_clears_all_items(self):
        self.cache.set('a', 'apple')
        self.cache.set('b', 'banana')
        result = self.cache.cleanup()
        self.assertEqual(result, "Cleaned successfully")
        self.assertIsNone(self.cache.get('a'))
        self.assertIsNone(self.cache.get('b'))

    def test_ttl_expiration(self):
        self.cache.set('short_lived', 'data', ttl=1)
        time.sleep(0.01)
        self.cache.set('long_lived', 'data', ttl=10000)
        
        self.cache.set('instant_expire', 'data', ttl=0)
        self.assertIsNone(self.cache.get('instant_expire'))
        
        self.cache.set('wait_item', 'data', ttl=10)
        time.sleep(0.1)
        self.assertEqual(self.cache.get('wait_item'), 'data')

if __name__ == '__main__':
    unittest.main()