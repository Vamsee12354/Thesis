from implementation_manual import Product_cache_get
import unittest

class TestProductCacheGet(unittest.TestCase):

    def setUp(self):
        self.expiry_time = 60000
        self.cache = Product_cache_get(self.expiry_time)

    def test_initialization(self):
        self.assertIsInstance(self.cache, Product_cache_get)

    def test_set_and_get(self):
        self.cache.set('a', 'apple')
        self.assertEqual(self.cache.get('a'), 'apple')

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.cache.get('nonexistent'))

    def test_set_with_custom_ttl(self):
        custom_ttl = 1000
        self.cache.set('fruit', {'id': 'fruit', 'name': 'apple'}, ttl=custom_ttl)
        self.assertEqual(self.cache.get('fruit'), {'id': 'fruit', 'name': 'apple'})

    def test_set_with_negative_ttl(self):
        self.cache.set('temp', 'temporary', ttl=-1)
        self.assertIsNone(self.cache.get('temp'))

    def test_delete_existing_key(self):
        self.cache.set('a', 'apple')
        result = self.cache.delete('a')
        self.assertEqual(result, 'deleted successfully')
        self.assertIsNone(self.cache.get('a'))

    def test_delete_nonexistent_key(self):
        result = self.cache.delete('nonexistent')
        self.assertEqual(result, 'deleted successfully')

    def test_cleanup(self):
        self.cache.set('a', 'apple')
        self.cache.set('b', 'banana')
        result = self.cache.cleanup()
        self.assertEqual(result, 'Cleaned successfully')
        self.assertIsNone(self.cache.get('a'))
        self.assertIsNone(self.cache.get('b'))

    def test_cleanup_empty_cache(self):
        result = self.cache.cleanup()
        self.assertEqual(result, 'Cleaned successfully')

if __name__ == '__main__':
    unittest.main()