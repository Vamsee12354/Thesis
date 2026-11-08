from implementation_manual import Product_cache_get
import unittest
import time

class TestProductCacheGet(unittest.TestCase):

    def setUp(self):
        self.expiry_time = 1000
        self.cache = Product_cache_get(self.expiry_time)

    def test_initialization(self):
        self.assertIsInstance(self.cache, Product_cache_get)

    def test_set_and_get_happy_path(self):
        key = 'product1'
        value = {'id': '1', 'name': 'apple'}
        self.cache.set(key, value)
        result = self.cache.get(key)
        self.assertEqual(result, value)

    def test_get_nonexistent_key(self):
        result = self.cache.get('nonexistent')
        self.assertIsNone(result)

    def test_set_with_negative_ttl(self):
        key = 'product2'
        value = {'id': '2', 'name': 'banana'}
        self.cache.set(key, value, ttl=-1)
        result = self.cache.get(key)
        self.assertIsNone(result)

    def test_set_with_custom_ttl(self):
        key = 'product3'
        value = {'id': '3', 'name': 'orange'}
        custom_ttl = 500
        self.cache.set(key, value, ttl=custom_ttl)
        result = self.cache.get(key)
        self.assertEqual(result, value)
        time.sleep(0.6)
        result = self.cache.get(key)
        self.assertIsNone(result)

    def test_delete_existing_key(self):
        key = 'product4'
        value = {'id': '4', 'name': 'grape'}
        self.cache.set(key, value)
        result = self.cache.delete(key)
        self.assertEqual(result, "deleted successfully")
        self.assertIsNone(self.cache.get(key))

    def test_delete_nonexistent_key(self):
        result = self.cache.delete('nonexistent')
        self.assertEqual(result, "deleted successfully")

    def test_cleanup(self):
        keys = ['product5', 'product6']
        values = [{'id': '5', 'name': 'mango'}, {'id': '6', 'name': 'kiwi'}]
        for key, value in zip(keys, values):
            self.cache.set(key, value)
        result = self.cache.cleanup()
        self.assertEqual(result, "Cleaned successfully")
        for key in keys:
            self.assertIsNone(self.cache.get(key))

    def test_cleanup_empty_cache(self):
        result = self.cache.cleanup()
        self.assertEqual(result, "Cleaned successfully")

    def test_ttl_expiry(self):
        key = 'product7'
        value = {'id': '7', 'name': 'pear'}
        self.cache.set(key, value, ttl=100)
        time.sleep(0.2)
        result = self.cache.get(key)
        self.assertIsNone(result)

    def test_multiple_sets_same_key(self):
        key = 'product8'
        value1 = {'id': '8', 'name': 'plum'}
        value2 = {'id': '8', 'name': 'plum_updated'}
        self.cache.set(key, value1)
        self.cache.set(key, value2)
        result = self.cache.get(key)
        self.assertEqual(result, value2)

if __name__ == '__main__':
    unittest.main()