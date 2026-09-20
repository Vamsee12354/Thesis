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

    def test_set_without_ttl(self):
        result = self.cache.set('a', 'apple')
        self.assertIsNone(result)
        self.assertEqual(self.cache.get('a'), 'apple')

    def test_set_with_positive_ttl(self):
        result = self.cache.set('fruit', {'id': 'fruit', 'name': 'apple'}, ttl=60000)
        self.assertIsNone(result)
        self.assertEqual(self.cache.get('fruit'), {'id': 'fruit', 'name': 'apple'})

    def test_set_with_zero_ttl(self):
        result = self.cache.set('zero_ttl', 'value', ttl=0)
        self.assertIsNone(result)
        self.assertIsNone(self.cache.get('zero_ttl'))

    def test_set_with_negative_ttl(self):
        result = self.cache.set('negative_ttl', 'value', ttl=-1000)
        self.assertIsNone(result)
        self.assertIsNone(self.cache.get('negative_ttl'))

    def test_set_overwrites_existing_value(self):
        self.cache.set('a', 'apple')
        self.cache.set('a', 'banana')
        self.assertEqual(self.cache.get('a'), 'banana')

class TestProductCacheGetGet(unittest.TestCase):
    def setUp(self):
        self.cache = Product_cache_get(expiry_time=60000)
        self.cache.set('a', 'apple')
        self.cache.set('b', 'banana', ttl=100)

    def test_get_existing_key(self):
        self.assertEqual(self.cache.get('a'), 'apple')

    def test_get_existing_key_with_ttl(self):
        time.sleep(0.11)
        self.assertIsNone(self.cache.get('b'))

    def test_get_non_existent_key(self):
        self.assertIsNone(self.cache.get('nonexistent'))

class TestProductCacheGetDelete(unittest.TestCase):
    def setUp(self):
        self.cache = Product_cache_get(expiry_time=60000)
        self.cache.set('a', 'apple')

    def test_delete_existing_key(self):
        result = self.cache.delete('a')
        self.assertEqual(result, 'deleted successfully')
        self.assertIsNone(self.cache.get('a'))

    def test_delete_non_existent_key(self):
        result = self.cache.delete('nonexistent')
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
        self.assertIsNone(cache.get('nonexistent'))

    def test_set_and_get_with_none_value(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('none_value', None)
        self.assertIsNone(cache.get('none_value'))

    def test_multiple_sets_with_different_ttls(self):
        cache = Product_cache_get(expiry_time=60000)
        cache.set('a', 'apple', ttl=100)
        cache.set('b', 'banana', ttl=200)
        cache.set('c', 'cherry')
        self.assertEqual(cache.get('a'), 'apple')
        self.assertEqual(cache.get('b'), 'banana')
        self.assertEqual(cache.get('c'), 'cherry')