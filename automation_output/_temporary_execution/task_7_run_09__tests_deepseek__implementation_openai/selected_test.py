import unittest
from implementation_manual import shopping_list

class TestShoppingList(unittest.TestCase):
    def test_normal_functionality(self):
        products = [{"title": "Item1"}, {"title": "Item2"}, {"title": "Item3"}, {"title": "Item4"}]
        expected = '<ul><li>Item1</li><li>Item2</li><li>Item3</li><li>Item4</li></ul>'
        self.assertEqual(shopping_list(products), expected)

    def test_empty_shopping_list(self):
        self.assertEqual(shopping_list([]), '<ul></ul>')

    def test_html_in_titles(self):
        products = [{"title": "<strong>Item1</strong>"}, {"title": "<em>Item2</em>"}]
        expected = '<ul><li><strong>Item1</strong></li><li><em>Item2</em></li></ul>'
        self.assertEqual(shopping_list(products), expected)

    def test_single_item_list(self):
        products = [{"title": "SingleItem"}]
        expected = '<ul><li>SingleItem</li></ul>'
        self.assertEqual(shopping_list(products), expected)