# Tests for task9_product_cache_get
import unittest
import time 
from implementation_manual import Product_cache_get
class TestProductCache(unittest.TestCase):
    def test_set_and_get(self):
        cache=Product_cache_get( expiry_time=60)
        cache.set('a','apple')
        self.assertEqual(cache.get('a'),'apple')

    def test_set_get_cleanup(self):
        cache=Product_cache_get( expiry_time=3)
        cache.set('a','apple')
        time.sleep(4)
        self.assertEqual(cache.get('a'),None)

    def test_set_get_delete(self):
        cache=Product_cache_get( expiry_time=3)
        cache.set('a','apple')
        cache.delete('a')
        self.assertEqual(cache.get('a'),None)

    def test_sleep_lesser_than_expiry_time(self):
        cache=Product_cache_get( expiry_time=3)
        cache.set('a','apple')
        time.sleep(1)
        self.assertEqual(cache.get('a'),'apple')


    def test_sleep_more_than_expiry_time(self):
        cache=Product_cache_get( expiry_time=3)
        cache.set('a','apple')
        time.sleep(6)
        self.assertEqual(cache.get('a'),None)


    def test_same_item_dictionary(self):
        cache=Product_cache_get( expiry_time=60)
        cache.set('a','apple')
        cache.set('a','apple')
        self.assertEqual(cache.get('a'),'apple')

    def test_multiple_values(self):
        cache=Product_cache_get( expiry_time=60)
        cache.set('a','apple')
        cache.set('b','Bangkok')
        cache.set('c','Camel')
        answer={'a':'apple','b':'Bangkok','c':'Camel'}
        for key,value in answer.items():
            self.assertEqual(cache.get(key),value)

    def test_set_and_get_with_number_as_key(self):
        cache=Product_cache_get( expiry_time=60)
        cache.set(1,'apple')
        cache.set(2,'Bangkok')
        cache.set(3,'Camel')
        answer={1:'apple',2:'Bangkok',3:'Camel'}
        for key,value in answer.items():
            self.assertEqual(cache.get(key),value)

    def test_set_and_get_with_other_language(self):
        cache=Product_cache_get( expiry_time=60)
        cache.set(1,'ఆపిల్')
        cache.set(2,'బ్యాంకాక్')
        cache.set(3,'ఒంటె')
        answer={1:'ఆపిల్',2:'బ్యాంకాక్',3:'ఒంటె'}
        for key,value in answer.items():
            self.assertEqual(cache.get(key),value)

    def test_delete_if_list_is_empty(self):
        cache=Product_cache_get( expiry_time=60)
        self.assertEqual(cache.delete('a'),'deleted successfully')


    def test_multiple_items_delete_in_one_go(self):
        cache=Product_cache_get( expiry_time=60)
        cache.set('a','apple')
        cache.set('a','apple')
        self.assertEqual(cache.delete('a'),'deleted successfully')

    def test_non_existent(self):
        cache=Product_cache_get( expiry_time=60)
        cache.delete('a')
        self.assertEqual(cache.get('a'),None)

    def test_first_del_then_set(self):
        cache=Product_cache_get( expiry_time=60)
        cache.delete('a')
        cache.set('a','apple')
        self.assertEqual(cache.delete('a'),'deleted successfully')

    def test_get_wrong_item(self):
        cache=Product_cache_get( expiry_time=60)
        cache.set('Fruit','apple')
        self.assertEqual(cache.get('fruit'),None)


    def test_cleanup(self):
        cache=Product_cache_get( expiry_time=5)
        cache.set('a','apple')
        time.sleep(7)
        cache.set('b','ball')
        cache.set('c','cat')
        time.sleep(8)
        cache.set('d','dog')
        cache.set('e','elephant')
        self.assertEqual(cache.cleanup(),'Cleaned successfully')
        

    def test_get_items_late(self):
        cache=Product_cache_get( expiry_time=4)
        cache.set('a','apple')
        time.sleep(6)
        cache.set('b','banana')
        answer={'a':None,'b':'banana'}
        for key,value in answer.items():
            self.assertEqual(cache.get(key),value)

    
    def test_very_large_expiry(self):
        cache = Product_cache_get(  expiry_time=999999999)
        cache.set('a', 'apple')
        self.assertEqual(cache.get('a'), 'apple')

    def test_set_expiry_zero(self):
        cache = Product_cache_get(  expiry_time=0)
        cache.set('a', 'apple')
        self.assertEqual(cache.get('a'),'apple') 

    

if __name__ == '__main__':
    unittest.main()