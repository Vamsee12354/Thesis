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

    def test_html_content_in_titles(self):
        products = [{"title": "<strong>Bold Item</strong>"}, {"title": "Item with & symbol"}]
        expected_output = '<ul><li>&lt;strong&gt;Bold Item&lt;/strong&gt;</li><li>Item with &amp; symbol</li></ul>'
        self.assertEqual(shopping_list(products), expected_output)

if __name__ == '__main__':
    unittest.main()
