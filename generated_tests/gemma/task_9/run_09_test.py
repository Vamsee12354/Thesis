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
        key = "expired_item"
        value = "banana"
        
        # Act
        self.cache.set(key, value, ttl=-100)
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
        self.cache.set('k2', 'v2')
        
        # Act
        status = self.cache.cleanup()
        val1 = self.cache.get('k1')
        val2 = self.cache.get('k2')
        
        # Assert
        self.assertEqual(status, "Cleaned successfully")
        self.assertIsNone(val1)
        self.assertIsNone(val2)

    def test_ttl_expiration(self):
        # Arrange
        # Use a very small TTL for testing expiration
        key = "short_lived"
        value = "temporary"
        short_ttl = 10 # 10ms
        
        # Act
        self.cache.set(key, value, ttl=short_ttl)
        # Wait for TTL to pass
        time.sleep(0.05)
        result = self.cache.get(key)
        
        # Assert
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()