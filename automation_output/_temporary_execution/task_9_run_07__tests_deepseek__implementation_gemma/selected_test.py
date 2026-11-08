import unittest
from implementation_manual import Product_cache_get
import time

class TestProductCacheGet(unittest.TestCase):
    def setUp(self):
        self.cache = Product_cache_get(expiry_time=60000)

    def test_initialization(self):
        self.assertIsInstance(self.cache, Product_cache_get)

    def test_set_and_get(self):
        self.cache.set('a', 'apple')
        self.assertEqual(self.cache.get('a'), 'apple')

    def test_get_non_existent_key(self):
        self.assertIsNone(self.cache.get('non-existent'))

    def test_set_with_custom_ttl(self):
        self.cache.set('fruit', {'id': 'fruit', 'name': 'apple'}, ttl=60000)
        self.assertEqual(self.cache.get('fruit'), {'id': 'fruit', 'name': 'apple'})

    def test_set_with_negative_ttl(self):
        self.cache.set('b', 'banana', ttl=-1000)
        self.assertIsNone(self.cache.get('b'))

    def test_delete(self):
        self.cache.set('a', 'apple')
        self.assertEqual(self.cache.delete('a'), 'deleted successfully')
        self.assertIsNone(self.cache.get('a'))

    def test_cleanup(self):
        self.cache.set('a', 'apple')
        self.cache.set('b', 'banana')
        self.assertEqual(self.cache.cleanup(), 'Cleaned successfully')
        self.assertIsNone(self.cache.get('a'))
        self.assertIsNone(self.cache.get('b'))

    def test_expiry(self):
        self.cache = Product_cache_get(expiry_time=1000)
        self.cache.set('a', 'apple')
        time.sleep(2)
        self.assertIsNone(self.cache.get('a'))

if __name__ == '__main__':
    unittest.main()