import unittest
from implementation_manual import shopping_list

class TestShoppingListFunction(unittest.TestCase):

    def test_normal_functionality(self):
        # Arrange
        products = [
            {"title": "Item1"},
            {"title": "Item2"},
            {"title": "Item3"},
            {"title": "Item4"}
        ]
        expected_html = "<ul><li>Item1</li><li>Item2</li><li>Item3</li><li>Item4</li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_html)

    def test_empty_shopping_list(self):
        # Arrange
        products = []
        expected_html = "<ul></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_html)

    def test_single_product(self):
        # Arrange
        products = [{"title": "SingleItem"}]
        expected_html = "<ul><li>SingleItem</li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_html)

    def test_html_content_in_title(self):
        # Arrange
        products = [{"title": "<b>BoldItem</b>"}]
        expected_html = "<ul><li><b>BoldItem</b></li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_html)

    def test_multiple_products_with_html_titles(self):
        # Arrange
        products = [
            {"title": "<i>Italic1</i>"},
            {"title": "<script>alert('x')</script>"},
            {"title": "NormalItem"}
        ]
        expected_html = "<ul><li><i>Italic1</i></li><li><script>alert('x')</script></li><li>NormalItem</li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_html)

    def test_titles_are_non_empty_and_non_none(self):
        # Arrange
        products = [
            {"title": "ValidTitle"},
            {"title": "AnotherTitle"}
        ]
        expected_html = "<ul><li>ValidTitle</li><li>AnotherTitle</li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_html)

if __name__ == "__main__":
    unittest.main()