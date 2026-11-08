# Tests for task7_product_list_live_v
import unittest
from implementation_manual import shopping_list

class Test_get_shopping_list(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(shopping_list([]),"<ul></ul>")

    def test_normal_functionality(self):
        self.assertEqual(shopping_list([{"title":"Banana"},{"title":"Apple"},{"title":"Mango"},{"title":"Avacado"}]),"<ul><li>Banana</li><li>Apple</li><li>Mango</li><li>Avacado</li></ul>")

    def test_other_language_functionality(self):
        self.assertEqual(shopping_list([{"title":"Plátano"},{"title":"Mango"},{"title":"Manzana"},{"title":"Aguacate"}]),"<ul><li>Plátano</li><li>Mango</li><li>Manzana</li><li>Aguacate</li></ul>")

    def test_single_product(self):
        self.assertEqual(shopping_list([{"title":"Mango"}]),"<ul><li>Mango</li></ul>")

    def test_check_same_product_repeating(self):
        self.assertEqual(shopping_list([{"title":"Banana"},{"title":"Banana"},{"title":"Banana"},{"title":"Banana"},{"title":"Banana"}]),"<ul><li>Banana</li><li>Banana</li><li>Banana</li><li>Banana</li><li>Banana</li></ul>")

    def test_symbols_as_shopping_list(self):
        self.assertEqual(shopping_list([{"title":"!"},{"title":"@"},{"title":"%"},{"title":"^"},{"title":"&"},{"title":"*"}]),"<ul><li>!</li><li>@</li><li>%</li><li>^</li><li>&</li><li>*</li></ul>")

    def test_title_functionality(self):
        self.assertEqual(shopping_list([{"title1":"Sample Product 1"},{"title2":"Sample Product 2"},{"title":"Sample Product 3"}]),"<ul><li>Sample Product 3</li></ul>")

    def test_number_functionality(self):
        self.assertEqual(shopping_list([{"title":1},{"title":16},{"title":56}]),"<ul><li>1</li><li>16</li><li>56</li></ul>")

    def test_title_caps(self):
        self.assertEqual(shopping_list([{"TITLE":"Plátano"},{"title":"Mango"},{"Title":"Manzana"},{"TiTlE":"Aguacate"}]),"<ul><li>Mango</li></ul>")

    def test_title_no_information(self):
        self.assertEqual(shopping_list([{'title':'','title':'','title':''}]),'<ul></ul>')


if __name__ == "__main__":
    unittest.main()