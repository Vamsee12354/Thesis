from implementation_manual import shopping_list
import unittest

class TestShoppingList(unittest.TestCase):

    def test_normal_functionality(self):
        products = [{"title":"Item1"},{"title":"Item2"},{"title":"Item3"},{"title":"Item4"}]
        result = shopping_list(products)
        expected = "<ul><li>Item1</li><li>Item2</li><li>Item3</li><li>Item4</li></ul>"
        self.assertEqual(result, expected)

    def test_empty_list(self):
        result = shopping_list([])
        expected = "<ul></ul>"
        self.assertEqual(result, expected)

    def test_single_product(self):
        products = [{"title":"SingleItem"}]
        result = shopping_list(products)
        expected = "<ul><li>SingleItem</li></ul>"
        self.assertEqual(result, expected)

    def test_product_with_html_in_title(self):
        products = [{"title":"<b>Bold</b> Item"}]
        result = shopping_list(products)
        expected = "<ul><li><b>Bold</b> Item</li></ul>"
        self.assertEqual(result, expected)

    def test_multiple_products_with_html_in_title(self):
        products = [{"title":"<i>Italic</i> Item"}, {"title":"<u>Underline</u> Item"}]
        result = shopping_list(products)
        expected = "<ul><li><i>Italic</i> Item</li><li><u>Underline</u> Item</li></ul>"
        self.assertEqual(result, expected)

    def test_product_without_title_key(self):
        products = [{"name":"NoTitleItem"}]
        with self.assertRaises(KeyError):
            shopping_list(products)

    def test_product_with_none_title(self):
        products = [{"title": None}]
        with self.assertRaises(TypeError):
            shopping_list(products)

    def test_product_with_empty_title(self):
        products = [{"title": ""}]
        result = shopping_list(products)
        expected = "<ul><li></li></ul>"
        self.assertEqual(result, expected)