import unittest
from implementation_manual import Product_cache_get
import time

class TestProductCacheGet(unittest.TestCase):
    def setUp(self):
        self.cache = Product_cache_get(expiry_time=1000)

    def test_initialization(self):
        self.assertIsInstance(self.cache, Product_cache_get)

    def test_set_and_get(self):
        self.cache.set('a', 'apple')
        self.assertEqual(self.cache.get('a'), 'apple')

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.cache.get('nonexistent'))

    def test_set_with_ttl(self):
        self.cache.set('fruit', {'id': 'fruit', 'name': 'apple'}, ttl=100)
        self.assertEqual(self.cache.get('fruit'), {'id': 'fruit', 'name': 'apple'})
        time.sleep(0.2)
        self.assertIsNone(self.cache.get('fruit'))

    def test_set_with_negative_ttl(self):
        self.cache.set('b', 'banana', ttl=-100)
        self.assertIsNone(self.cache.get('b'))

    def test_delete(self):
        self.cache.set('a', 'apple')
        self.assertEqual(self.cache.delete('a'), 'deleted successfully')
        self.assertIsNone(self.cache.get('a'))

    def test_delete_nonexistent_key(self):
        self.assertEqual(self.cache.delete('nonexistent'), 'deleted successfully')

    def test_cleanup(self):
        self.cache.set('a', 'apple')
        self.cache.set('b', 'banana')
        self.assertEqual(self.cache.cleanup(), 'Cleaned successfully')
        self.assertIsNone(self.cache.get('a'))
        self.assertIsNone(self.cache.get('b'))

    def test_expiry(self):
        self.cache.set('a', 'apple')
        time.sleep(1.1)
        self.assertIsNone(self.cache.get('a'))