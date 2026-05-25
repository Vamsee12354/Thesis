# Tests for task7_product_list_live_v
import unittest
from implementation_manual import shopping_list

class Test_get_shopping_list(unittest.TestCase):
    def test_no_text(self):
        self.assertEqual(shopping_list(""),False)

    def test_normal_functionality(self):
        self.assertEqual(shopping_list(["Banana","Apple","Mango","Avacado"]),"<ul><li>Banana</li><li>Apple</li><li>Mango</li><li>Avacado</li></ul>")

    def test_other_language_functionality(self):
        self.assertEqual(shopping_list(["Plátano","Mango","Manzana","Aguacate"]),"<ul><li>Plátano</li><li>Mango</li><li>Manzana</li><li>Aguacate</li></ul>")

    def test_shoppinglist_as_single_string(self):
        self.assertEqual(shopping_list("Plátano Mango Manzana Aguacate"),"<ul><li>Plátano</li><li>Mango</li><li>Manzana</li><li>Aguacate</li></ul>")

    def test_shopping_list_with_quantity(self):
        self.assertEqual(shopping_list({"Plátano":2,"Mango":7,"Manzana":11,"Aguacate":13}),"<ul><li>Plátano</li><li>Mango</li><li>Manzana</li><li>Aguacate</li></ul>")

    def test_check_same_product_repeating(self):
        self.assertEqual(shopping_list(["Banana","Banana","Banana","Banana","Banana"]),"<ul><li>Banana</li><li>Banana</li><li>Banana</li><li>Banana</li><li>Banana</li></ul>")

    def test_number_as_shopping_list(self):
        self.assertEqual(shopping_list([1,2,3,4,5,6]),"<ul><li>1</li><li>2</li><li>3</li><li>4</li><li>5</li><li>6</li></ul>")

    def test_symbols_as_shopping_list(self):
        self.assertEqual(shopping_list(["!","@","%","^","&","*"]),"<ul><li>!</li><li>@</li><li>%</li><li>^</li><li>&</li><li>*</li></ul>")

    def test_multiple_blanks(self):
        self.assertEqual(shopping_list(["","","",""]),"<ul><li></li><li></li><li></li><li></li></ul>")

     def test_normal_functionality(self):
        self.assertEqual(shopping_list(["Banana","Apple","Mango","Avacado"]),"<ul><li>Banana</li><li>Apple</li><li>Mango</li><li>Avacado</li></ul>")

    



if __name__ == "__main__":
    unittest.main()