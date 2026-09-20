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

    def test_set_and_get_basic_value(self):
        self.cache.set('a', 'apple')
        self.assertEqual(self.cache.get('a'), 'apple')

    def test_set_with_custom_ttl(self):
        self.cache.set('fruit', {'id': 'fruit', 'name': 'apple'}, ttl=60000)
        self.assertEqual(self.cache.get('fruit'), {'id': 'fruit', 'name': 'apple'})

    def test_set_with_negative_ttl(self):
        self.cache.set('temp', 'temporary', ttl=-1000)
        self.assertIsNone(self.cache.get('temp'))

    def test_set_overwrites_existing_value(self):
        self.cache.set('a', 'apple')
        self.cache.set('a', 'banana')
        self.assertEqual(self.cache.get('a'), 'banana')

    def test_set_with_zero_ttl(self):
        self.cache.set('zero_ttl', 'value', ttl=0)
        self.assertIsNone(self.cache.get('zero_ttl'))

class TestProductCacheGetGet(unittest.TestCase):
    def setUp(self):
        self.cache = Product_cache_get(expiry_time=60000)
        self.cache.set('a', 'apple')

    def test_get_existing_key(self):
        self.assertEqual(self.cache.get('a'), 'apple')

    def test_get_non_existent_key(self):
        self.assertIsNone(self.cache.get('non_existent'))

    def test_get_expired_key(self):
        self.cache.set('expired', 'value', ttl=1)
        time.sleep(0.002)
        self.assertIsNone(self.cache.get('expired'))

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
    def test_get_before_set(self):
        cache = Product_cache_get(expiry_time=60000)
        self.assertIsNone(cache.get('any_key'))

    def test_multiple_sets_and_gets(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('1', 'one')
        cache.set('2', 'two')
        cache.set('3', 'three')
        self.assertEqual(cache.get('1'), 'one')
        self.assertEqual(cache.get('2'), 'two')
        self.assertEqual(cache.get('3'), 'three')

    def test_ttl_with_large_value(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('long', 'value', ttl=3600000)
        self.assertEqual(cache.get('long'), 'value')

    def test_ttl_with_small_value(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('short', 'value', ttl=1)
        time.sleep(0.002)
        self.assertIsNone(cache.get('short'))