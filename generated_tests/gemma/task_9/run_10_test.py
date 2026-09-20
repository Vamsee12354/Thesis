import unittest
import time
from implementation_manual import Product_cache_get

class TestProductCacheGet(unittest.TestCase):

    def setUp(self):
        self.default_expiry = 60000
        self.cache = Product_cache_get(expiry_time=self.default_expiry)

    def test_init_initialization(self):
        # Verify instance is created
        self.assertIsInstance(self.cache, Product_cache_get)

    def test_set_and_get_happy_path(self):
        # Arrange
        key = 'a'
        value = 'apple'

        # Act
        self.cache.set(key, value)
        result = self.cache.get(key)

        # Assert
        self.assertEqual(result, value)

    def test_get_non_existent_key(self):
        # Act
        result = self.cache.get("non-existent")

        # Assert
        self.assertIsNone(result)

    def test_set_with_custom_ttl(self):
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
        key = 'expired_item'
        value = 'banana'
        ttl = -1

        # Act
        self.cache.set(key, value, ttl=ttl)
        result = self.cache.get(key)

        # Assert
        self.assertIsNone(result)

    def test_set_with_very_short_ttl(self):
        # Arrange
        key = 'quick_expire'
        value = 'gone'
        ttl = 1  # 1ms

        # Act
        self.cache.set(key, value, ttl=ttl)
        time.sleep(0.01)  # Wait for expiration
        result = self.cache.get(key)

        # Assert
        self.assertIsNone(result)

    def test_delete_existing_key(self):
        # Arrange
        key = 'a'
        self.cache.set(key, 'apple')

        # Act
        status = self.cache.delete(key)
        result = self.cache.get(key)

        # Assert
        self.assertEqual(status, "deleted successfully")
        self.assertIsNone(result)

    def test_cleanup_clears_all_items(self):
        # Arrange
        self.cache.set('k1', 'v1')
        self.cache.set('k2', 'v2', ttl=100000)

        # Act
        status = self.cache.cleanup()
        res1 = self.cache.get('k1')
        res2 = self.cache.get('k2')

        # Assert
        self.assertEqual(status, "Cleaned successfully")
        self.assertIsNone(res1)
        self.assertIsNone(res2)

if __name__ == '__main__':
    unittest.main()