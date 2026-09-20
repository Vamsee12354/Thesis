from implementation_manual import shopping_list
import unittest

class TestShoppingList(unittest.TestCase):

    def test_normal_functionality_with_multiple_items(self):
        products = [{"title": "Item1"}, {"title": "Item2"}, {"title": "Item3"}, {"title": "Item4"}]
        result = shopping_list(products)
        expected = "<ul><li>Item1</li><li>Item2</li><li>Item3</li><li>Item4</li></ul>"
        self.assertEqual(result, expected)

    def test_single_item_in_list(self):
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
        products = [{"title": "Item & More"}, {"title": "Item <Special>"}]
        result = shopping_list(products)
        expected = "<ul><li>Item & More</li><li>Item <Special></li></ul>"
        self.assertEqual(result, expected)

    def test_product_with_html_content_in_title(self):
        products = [{"title": "<b>Bold Item</b>"}, {"title": "<script>alert('xss')</script>"}]
        result = shopping_list(products)
        expected = "<ul><li><b>Bold Item</b></li><li><script>alert('xss')</script></li></ul>"
        self.assertEqual(result, expected)

    def test_product_with_unicode_characters_in_title(self):
        products = [{"title": "Item™"}, {"title": "Item¢"}]
        result = shopping_list(products)
        expected = "<ul><li>Item™</li><li>Item¢</li></ul>"
        self.assertEqual(result, expected)

    def test_product_with_empty_title(self):
        products = [{"title": ""}]
        result = shopping_list(products)
        expected = "<ul><li></li></ul>"
        self.assertEqual(result, expected)

    def test_product_with_none_title(self):
        products = [{"title": None}]
        result = shopping_list(products)
        expected = "<ul><li>None</li></ul>"
        self.assertEqual(result, expected)

    def test_product_with_missing_title_key(self):
        products = [{}]
        with self.assertRaises(KeyError):
            shopping_list(products)

    def test_product_with_non_string_title(self):
        products = [{"title": 123}]
        result = shopping_list(products)
        expected = "<ul><li>123</li></ul>"
        self.assertEqual(result, expected)