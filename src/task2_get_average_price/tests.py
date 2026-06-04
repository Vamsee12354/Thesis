# Tests for task2_get_average_price
import unittest
from implementation_manual import get_average


class Test_get_average_price(unittest.TestCase):
    def test_list_is_empty(self):
        self.assertEqual(get_average([]),[])

    def test_working_list_price(self):
        self.assertEqual(get_average([1.5,2,4,0,-3,3,5]),2.58)

    def test_negatives(self):
        self.assertFalse(get_average([-1,-3,-4.2,-1.3,-9.1]))

    def test_alphabets(self):
        self.assertFalse(get_average(['alex','ben','chem','don']))

    def test_alphanumericals(self):
        self.assertFalse(get_average(['@','!','#','$']))

    def test_highvalue_numbers(self):
        self.assertEqual(get_average([2313213123,1021232122.5323,20311111.76,101112321.21]),863967169.63 )

    def test_zero_value(self):
        self.assertEqual(get_average([0,0]),0)

    
    def test_null_value(self):
        self.assertEqual(get_average([12,1232,None,132]),458.67)

    
    def test_multiple_nulls(self):
        self.assertEqual(get_average([None,None]),0)

if __name__ == "__main__":
    unittest.main()
