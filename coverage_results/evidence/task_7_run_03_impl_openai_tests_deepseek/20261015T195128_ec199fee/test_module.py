import unittest
from implementation_manual import shopping_list

class TestShoppingList(unittest.TestCase):
    def test_normal_functionality(self):
        products = [{"title": "Item1"}, {"title": "Item2"}, {"title": "Item3"}, {"title": "Item4"}]
        expected_output = "<ul><li>Item1</li><li>Item2</li><li>Item3</li><li>Item4</li></ul>"
        self.assertEqual(shopping_list(products), expected_output)

    def test_empty_shopping_list(self):
        products = []
        expected_output = "<ul></ul>"
        self.assertEqual(shopping_list(products), expected_output)

    def test_html_in_titles(self):
        products = [{"title": "<b>Item1</b>"}, {"title": "<i>Item2</i>"}]
        expected_output = "<ul><li><b>Item1</b></li><li><i>Item2</i></li></ul>"
        self.assertEqual(shopping_list(products), expected_output)

    def test_single_item(self):
        products = [{"title": "Item1"}]
        expected_output = "<ul><li>Item1</li></ul>"
        self.assertEqual(shopping_list(products), expected_output)