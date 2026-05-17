# Tests for task3_get_min_attribute
import unittest
from implementation_manual import get_min

class Test_get_min(unittest.TestCase):
    def test_functioning(self):
        self.assertEqual(get_min({"Mercedes":75000,"Toyota":23000,"Honda":15000,"Audi":67000,"BMV":80000}),("Honda", 15000))

    def test_check_what_if_equal_rates(self):
        self.assertEqual(get_min({"Mercedes":75000,"Toyota":75000,"Honda":75000,"Audi":75000,"BMV":75000}),("Mercedes", 75000)) 

    def test_negative_items(self):
        self.assertEqual(get_min({"Mercedes":-75000,"Toyota":-23000,"Honda":-15000,"Audi":2000,"BMV":1000}),("BMV", 1000))
        
    def test_null_values(self):
        self.assertEqual(get_min({"Mercedes":None,"Toyota":None,"Honda":None,"Audi":"","BMV":None}),("Audi",""))
    
    def test_get_multiple_options_same_cost(self):
        self.assertEqual(get_min({"Mercedes":1000,"Toyota":1000,"Honda":3500,"Audi":2100,"BMV":7500}),({"Mercedes":1000,"Toyota":1000}))

    def test_handle_string(self):
        self.assertEqual(get_min({"Mercedes":"Seventy-Five Thousand","Toyota":"Twenty Three Thousand","Honda":"Fifteen Thousand","Audi":"Sixty Seven Thousand","BMV":"Eighty Thousand"}),("Honda", "Fifteen Thousand"))

    def test_handle_multiple_currencies(self):
        self.assertEqual(get_min({"Mercedes":"75000$","Toyota":"23000€","Honda":"15000£","Audi":"67000₹","BMV":"80000CHF"}),("Honda", "15000£"))

    def test_big_numbers(self):
        self.assertEqual(get_min({"Mercedes":10**10,"Toyota":20**15,"Honda":30**10,"Audi":15**12,"BMV":19**18}),("Mercedes",10**10))

        

if __name__ == "__main__":
    unittest.main()