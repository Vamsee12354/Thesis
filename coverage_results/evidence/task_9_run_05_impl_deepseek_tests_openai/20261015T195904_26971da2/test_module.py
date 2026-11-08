import unittest
import time
from implementation_manual import Product_cache_get

class TestProductCacheGet(unittest.TestCase):

    def setUp(self):
        self.default_ttl = 60000
        self.cache = Product_cache_get(expiry_time=self.default_ttl)

    def test_initialization(self):
        self.assertIsInstance(self.cache, Product_cache_get)

    def test_set_and_get_value(self):
        # Arrange
        key = 'a'
        value = 'apple'
        # Act
        self.cache.set(key, value)
        result = self.cache.get(key)
        # Assert
        self.assertEqual(result, value)

    def test_get_non_existent_key_returns_none(self):
        # Act
        result = self.cache.get("non-existent")
        # Assert
        self.assertIsNone(result)

    def test_set_with_custom_ttl_and_get(self):
        # Arrange
        key = "fruit"
        value = {"id": "fruit", "name": "apple"}
        custom_ttl = 60000
        # Act
        self.cache.set(key, value, ttl=custom_ttl)
        result = self.cache.get(key)
        # Assert
        self.assertEqual(result, value)

    def test_set_with_negative_ttl_invalidates_immediately(self):
        # Arrange
        key = "invalid"
        value = "data"
        negative_ttl = -1000
        # Act
        self.cache.set(key, value, ttl=negative_ttl)
        result = self.cache.get(key)
        # Assert
        self.assertIsNone(result)

    def test_delete_existing_key(self):
        # Arrange
        key = 'a'
        value = 'apple'
        self.cache.set(key, value)
        # Act
        result = self.cache.delete(key)
        get_after_delete = self.cache.get(key)
        # Assert
        self.assertEqual(result, "deleted successfully")
        self.assertIsNone(get_after_delete)

    def test_delete_non_existent_key(self):
        # Act
        result = self.cache.delete("non-existent")
        # Assert
        self.assertEqual(result, "deleted successfully")

    def test_cleanup_clears_all_cache(self):
        # Arrange
        self.cache.set('a', 'apple')
        self.cache.set('b', 'banana')
        # Act
        result = self.cache.cleanup()
        get_a = self.cache.get('a')
        get_b = self.cache.get('b')
        # Assert
        self.assertEqual(result, "Cleaned successfully")
        self.assertIsNone(get_a)
        self.assertIsNone(get_b)

    def test_expiry_of_cache_item(self):
        # Arrange
        key = 'temp'
        value = 'data'
        short_ttl = 100  # 100 milliseconds
        self.cache.set(key, value, ttl=short_ttl)
        # Act
        time.sleep(0.15)  # Sleep 150 milliseconds to expire the item
        result = self.cache.get(key)
        # Assert
        self.assertIsNone(result)

    def test_set_without_ttl_uses_default_expiry(self):
        # Arrange
        key = 'default_ttl_key'
        value = 'default_value'
        self.cache.set(key, value)
        # Act
        result = self.cache.get(key)
        # Assert
        self.assertEqual(result, value)

if __name__ == '__main__':
    unittest.main()