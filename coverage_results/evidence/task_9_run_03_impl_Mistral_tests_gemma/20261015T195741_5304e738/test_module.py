import unittest
import time
from implementation_manual import Product_cache_get

class TestProductCacheGet(unittest.TestCase):

    def setUp(self):
        self.default_expiry = 60000
        self.cache = Product_cache_get(expiry_time=self.default_expiry)

    def test_init_initialization(self):
        # Verify instance creation
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
        # Arrange
        key = 'non-existent'

        # Act
        result = self.cache.get(key)

        # Assert
        self.assertIsNone(result)

    def test_set_with_custom_ttl(self):
        # Arrange
        key = 'fruit'
        value = {"id": "fruit", "name": "apple"}
        custom_ttl = 1000  # 1 second

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

    def test_set_item_expires_after_ttl(self):
        # Arrange
        key = 'short_lived'
        value = 'temporary'
        ttl = 10  # 10ms

        # Act
        self.cache.set(key, value, ttl=ttl)
        time.sleep(0.02)  # Wait for expiration
        result = self.cache.get(key)

        # Assert
        self.assertIsNone(result)

    def test_delete_existing_key(self):
        # Arrange
        key = 'a'
        self.cache.set(key, 'apple')

        # Act
        result = self.cache.delete(key)

        # Assert
        self.assertEqual(result, "deleted successfully")
        self.assertIsNone(self.cache.get(key))

    def test_cleanup_clears_all_items(self):
        # Arrange
        self.cache.set('k1', 'v1')
        self.cache.set('k2', 'v2')
        self.cache.set('k3', 'v3', ttl=100000)

        # Act
        result = self.cache.cleanup()

        # Assert
        self.assertEqual(result, "Cleaned successfully")
        self.assertIsNone(self.cache.get('k1'))
        self.assertIsNone(self.cache.get('k2'))
        self.assertIsNone(self.cache.get('k3'))

    def test_complex_data_types(self):
        # Arrange
        key = 'user_1'
        value = {'id': 1, 'roles': ['admin', 'editor'], 'active': True}

        # Act
        self.cache.set(key, value)
        result = self.cache.get(key)

        # Assert
        self.assertEqual(result, value)
        self.assertEqual(result['roles'][0], 'admin')

if __name__ == '__main__':
    unittest.main()