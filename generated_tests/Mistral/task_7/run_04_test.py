from implementation_manual import shopping_list
import unittest

class TestShoppingList(unittest.TestCase):

    def test_normal_functionality_with_multiple_products(self):
        products = [
            {"title": "Item1"},
            {"title": "Item2"},
            {"title": "Item3"},
            {"title": "Item4"}
        ]
        result = shopping_list(products)
        expected = "<ul><li>Item1</li><li>Item2</li><li>Item3</li><li>Item4</li></ul>"
        self.assertEqual(result, expected)

    def test_single_product_in_list(self):
        products = [{"title": "SingleItem"}]
        result = shopping_list(products)
        expected = "<ul><li>SingleItem</li></ul>"
        self.assertEqual(result, expected)

    def test_empty_shopping_list(self):
        products = []
        result = shopping_list(products)
        expected = "<ul></ul>"
        self.assertEqual(result, expected)

    def test_product_with_special_characters_in_title(self):
        products = [{"title": "Item & More"}]
        result = shopping_list(products)
        expected = "<ul><li>Item & More</li></ul>"
        self.assertEqual(result, expected)

    def test_product_with_html_in_title(self):
        products = [{"title": "<b>Bold Item</b>"}]
        result = shopping_list(products)
        expected = "<ul><li><b>Bold Item</b></li></ul>"
        self.assertEqual(result, expected)

    def test_product_with_unicode_in_title(self):
        products = [{"title": "Item with émojis 😀"}]
        result = shopping_list(products)
        expected = "<ul><li>Item with émojis 😀</li></ul>"
        self.assertEqual(result, expected)

    def test_multiple_products_with_mixed_titles(self):
        products = [
            {"title": "Normal Item"},
            {"title": "Item & More"},
            {"title": "<i>Italic Item</i>"},
            {"title": "Item with émojis 😀"}
        ]
        result = shopping_list(products)
        expected = "<ul><li>Normal Item</li><li>Item & More</li><li><i>Italic Item</i></li><li>Item with émojis 😀</li></ul>"
        self.assertEqual(result, expected)