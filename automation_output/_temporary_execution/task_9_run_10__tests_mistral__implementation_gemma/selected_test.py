from implementation_manual import Product_cache_get
import unittest
import time

class TestProductCacheGetInitialization(unittest.TestCase):
    def test_init_with_positive_expiry_time(self):
        cache = Product_cache_get(expiry_time=60000)
        self.assertEqual(cache.expiry_time, 60000)

    def test_init_with_zero_expiry_time(self):
        cache = Product_cache_get(expiry_time=0)
        self.assertEqual(cache.expiry_time, 0)

    def test_init_with_negative_expiry_time(self):
        cache = Product_cache_get(expiry_time=-1000)
        self.assertEqual(cache.expiry_time, -1000)

class TestProductCacheGetSet(unittest.TestCase):
    def setUp(self):
        self.cache = Product_cache_get(expiry_time=60000)

    def test_set_with_string_value(self):
        self.cache.set('a', 'apple')
        self.assertEqual(self.cache.get('a'), 'apple')

    def test_set_with_dict_value(self):
        value = {'id': 'fruit', 'name': 'apple'}
        self.cache.set('fruit', value)
        self.assertEqual(self.cache.get('fruit'), value)

    def test_set_with_negative_ttl(self):
        self.cache.set('temp', 'temporary', ttl=-1000)
        self.assertIsNone(self.cache.get('temp'))

    def test_set_with_zero_ttl(self):
        self.cache.set('temp', 'temporary', ttl=0)
        self.assertIsNone(self.cache.get('temp'))

    def test_set_with_custom_ttl(self):
        self.cache.set('custom', 'value', ttl=50)
        time.sleep(0.1)
        self.assertIsNone(self.cache.get('custom'))

    def test_set_overwrites_existing_key(self):
        self.cache.set('a', 'apple')
        self.cache.set('a', 'banana')
        self.assertEqual(self.cache.get('a'), 'banana')

class TestProductCacheGetGet(unittest.TestCase):
    def setUp(self):
        self.cache = Product_cache_get(expiry_time=60000)
        self.cache.set('a', 'apple')

    def test_get_existing_key(self):
        self.assertEqual(self.cache.get('a'), 'apple')

    def test_get_non_existent_key(self):
        self.assertIsNone(self.cache.get('non_existent'))

    def test_get_expired_key(self):
        self.cache.set('temp', 'value', ttl=50)
        time.sleep(0.1)
        self.assertIsNone(self.cache.get('temp'))

class TestProductCacheGetDelete(unittest.TestCase):
    def setUp(self):
        self.cache = Product_cache_get(expiry_time=60000)
        self.cache.set('a', 'apple')

    def test_delete_existing_key(self):
        result = self.cache.delete('a')
        self.assertEqual(result, 'deleted successfully')
        self.assertIsNone(self.cache.get('a'))

    def test_delete_non_existent_key(self):
        result = self.cache.delete('non_existent')
        self.assertEqual(result, 'deleted successfully')

class TestProductCacheGetCleanup(unittest.TestCase):
    def setUp(self):
        self.cache = Product_cache_get(expiry_time=60000)
        self.cache.set('a', 'apple')
        self.cache.set('b', 'banana')

    def test_cleanup_removes_all_items(self):
        result = self.cache.cleanup()
        self.assertEqual(result, 'Cleaned successfully')
        self.assertIsNone(self.cache.get('a'))
        self.assertIsNone(self.cache.get('b'))

    def test_cleanup_on_empty_cache(self):
        empty_cache = Product_cache_get(expiry_time=60000)
        result = empty_cache.cleanup()
        self.assertEqual(result, 'Cleaned successfully')

class TestProductCacheGetEdgeCases(unittest.TestCase):
    def test_get_with_none_key(self):
        cache = Product_cache_get(expiry_time=60000)
        self.assertIsNone(cache.get(None))

    def test_set_with_none_key(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set(None, 'value')
        self.assertIsNone(cache.get(None))

    def test_set_with_none_value(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('key', None)
        self.assertIsNone(cache.get('key'))

    def test_multiple_operations(self):
        cache = Product_cache_get(expiry_time=100)
        cache.set('a', 'apple')
        cache.set('b', 'banana', ttl=50)
        self.assertEqual(cache.get('a'), 'apple')
        time.sleep(0.1)
        self.assertIsNone(cache.get('b'))
        self.assertEqual(cache.delete('a'), 'deleted successfully')
        self.assertIsNone(cache.get('a'))
        self.assertEqual(cache.cleanup(), 'Cleaned successfully')