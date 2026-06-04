# Tests for task3_get_min_attribute
import unittest
from implementation_manual import get_min_2_attributes

class Test_get_min(unittest.TestCase): 
    def test_get_min_2_attributes(self):
        data = [
    {"price":49.99,"battery_life":4.0},
    {"price":29.99,"battery_life":3.5},
    {"price":None,"battery_life":5.0},   
    {"battery_life": 2.0}                  
                ]
        self.assertEquals(get_min_2_attributes(data,"price"),29.99)

    def test_nulls_all_over(self):
        data = [
    {"price":None,"battery_life":None},
    {"price":None,"battery_life":None},
    {"price":None,"battery_life":None},   
    {"battery_life": None}                  
                ]
        self.assertFalse(get_min_2_attributes(data,"price"))

    def test_get_wrongname_attribute(self):
        data = [
    {"price":49.99,"battery_life":4.0},
    {"price":29.99,"battery_life":3.5},
    {"price":None,"battery_life":5.0},   
    {"battery_life": 2.0}                  
                ]
        self.assertFalse(get_min_2_attributes(data,"cost"))

    


    

  


        

if __name__ == "__main__":
    unittest.main()