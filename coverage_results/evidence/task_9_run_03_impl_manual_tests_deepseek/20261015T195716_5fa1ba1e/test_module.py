import unittest
from implementation_manual import Product_cache_get
import time

class TestProductCacheGet(unittest.TestCase):
    def setUp(self):
        self.cache = Product_cache_get(expiry_time=1000)

    def test_init(self):
        cache = Product_cache_get(expiry_time=5000)
        self.assertIsInstance(cache, Product_cache_get)

    def test_set_get(self):
        self.cache.set('test_key', 'test_value')
        self.assertEqual(self.cache.get('test_key'), 'test_value')

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.cache.get('nonexistent_key'))

    def test_set_with_ttl(self):
        self.cache.set('temp_key', 'temp_value', ttl=500)
        self.assertEqual(self.cache.get('temp_key'), 'temp_value')
        time.sleep(0.6)
        self.assertIsNone(self.cache.get('temp_key'))

    def test_set_with_negative_ttl(self):
        self.cache.set('invalid_key', 'invalid_value', ttl=-100)
        self.assertIsNone(self.cache.get('invalid_key'))

    def test_delete(self):
        self.cache.set('delete_key', 'delete_value')
        self.assertEqual(self.cache.delete('delete_key'), 'deleted successfully')
        self.assertIsNone(self.cache.get('delete_key'))

    def test_delete_nonexistent_key(self):
        self.assertEqual(self.cache.delete('nonexistent_key'), 'deleted successfully')

    def test_cleanup(self):
        self.cache.set('key1', 'value1')
        self.cache.set('key2', 'value2')
        self.assertEqual(self.cache.cleanup(), 'Cleaned successfully')
        self.assertIsNone(self.cache.get('key1'))
        self.assertIsNone(self.cache.get('key2'))

    def test_expiry(self):
        self.cache.set('expiring_key', 'expiring_value')
        time.sleep(1.1)
        self.assertIsNone(self.cache.get('expiring_key'))