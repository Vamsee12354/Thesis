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

    def test_equal_values(self):
        data = [
    {"price":49.99,"battery_life":49.99},
    {"price":49.99,"battery_life":49.99},
    {"price":49.99,"battery_life":49.99},   
    {"battery_life": 49.99}                  
                ]
        self.assertEquals(get_min_2_attributes(data,"battery_life"),49.99)

    def test_empty_list(self):
        data=[]
        self.assertEqual(get_min_2_attributes(data,"price"),None)   

    def test_with_one_value_in_dict(self):
        data=[
            
            {"price":49.99,},
            {"price":29.99,},
            {"price":None}   
            
        ]
        self.assertEqual(get_min_2_attributes(data,"price"),29.99)
        
    def test_diferent_langauge(self):
        data = [
    {"ధర":49.99,"రేటింగ్":4.0},
    {"ధర":29.99,"రేటింగ్":3.5},
    {"ధర":None,"రేటింగ్":5.0},   
    {"రేటింగ్": 2.0}                  
                ]
        self.assertEqual(get_min_2_attributes(data,"రేటింగ్"),2.0)


    def test_multiple_lines_different_keys_same_meaning(self):
        data=[
            {"price":249.99,"battery_life":9.99},
            {"usage":21.99,"review":4.99},
            {"cost":49.99,"battery":19.99},   
            {"battery": 429.99}                 
        ]
        self.assertEqual(get_min_2_attributes(data,'battery'),9.99)

        
    def test_multiple_lines_different_keys(self):
        data=[
            {"price":249.99,"battery_life":9.99},
            {"usage":21.99,"review":4.99},
            {"cost":49.99,"battery":19.99},   
            {"battery": 2.99}                 
        ]
        self.assertEqual(get_min_2_attributes(data,'battery'),2.99)
    


    

  


        

if __name__ == "__main__":
    unittest.main()