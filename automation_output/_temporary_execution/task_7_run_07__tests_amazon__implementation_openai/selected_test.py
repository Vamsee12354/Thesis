import unittest
from implementation_manual import shopping_list

class TestShoppingListView(unittest.TestCase):

    def test_normal_functionality(self):
        products = [{"title": "Item1"}, {"title": "Item2"}, {"title": "Item3"}, {"title": "Item4"}]
        expected_output = '<ul><li>Item1</li><li>Item2</li><li>Item3</li><li>Item4</li></ul>'
        self.assertEqual(shopping_list(products), expected_output)

    def test_empty_shopping_list(self):
        products = []
        expected_output = '<ul></ul>'
        self.assertEqual(shopping_list(products), expected_output)

    def test_single_product(self):
        products = [{"title": "Single Item"}]
        expected_output = '<ul><li>Single Item</li></ul>'
        self.assertEqual(shopping_list(products), expected_output)

    def test_html_in_title(self):
        products = [{"title": "<Bold>Item</Bold>"}]
        expected_output = '<ul><li>&lt;Bold&gt;Item&lt;/Bold&gt;</li></ul>'
        self.assertEqual(shopping_list(products), expected_output)

if __name__ == '__main__':
    unittest.main()
